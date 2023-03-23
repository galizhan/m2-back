from datetime import datetime

from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.utils import get_last_activity
from django.utils.translation import ugettext_lazy as _

User = get_user_model()
__all__ = ['PingView', ]


class PingView(generic.View):
    """
    This view is just in charge of returning the number of seconds since the
    'real last activity' that is maintained in the session by the middleware.
    """

    def get(self, request, *args, **kwargs):
        if '_session_security' not in request.session:
            # It probably has expired already
            return HttpResponse('"logout"', content_type='application/json')

        last_activity = get_last_activity(request.session)
        inactive_for = (datetime.now() - last_activity).seconds
        return HttpResponse(inactive_for, content_type='application/json')


class AdminAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
        'invalid_login1': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
    required_css_class = 'required'

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login1'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise ValidationError(self.error_messages['inactive'], code='inactive')
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                user.increment_wrong_pwd_count()
                raise self.get_invalid_login_error()
            else:
                user.clear_wrong_pwd_count()
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class AdminLogin(LoginView):
    template_name = 'admin/login.html'
    form_class = AdminAuthenticationForm


class AdminPasswordChangeView(PasswordChangeView):
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy('password_change_done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        user = self.request.user
        user.get_force_pwd_change()
        return super().form_valid(form)


class AdminPasswordChangeDoneView(PasswordChangeDoneView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        user = self.request.user
        user.create_password_history()
        user.clear_wrong_pwd_count()
        return super().dispatch(*args, **kwargs)
