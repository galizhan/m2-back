from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for M2.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(_("First Name"), blank=True, max_length=255, null=True)
    last_name = models.CharField(_("Last Name"), blank=True, max_length=255, null=True)
    phone_number = models.CharField(_("Phone Number"), blank=True, max_length=200, null=True)
    iin = models.CharField(_("IIN"), blank=True, max_length=200, null=True)
    avatar = models.FileField(null=True, blank=True, upload_to='users/avatars/')
    email = models.EmailField(_("Email Address"), blank=True, max_length=255)
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    gender = models.CharField(_("Gender"), blank=True, max_length=255, null=True)
    level = models.ForeignKey('main.Level', blank=True, null=True, on_delete=models.SET_NULL)
    investment_price = models.IntegerField(default=0, blank=True, null=True)
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
