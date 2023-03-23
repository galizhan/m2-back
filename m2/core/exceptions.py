from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError


class InvalidIIN(ValidationError):
    default_detail = _("Неверный ИИН")


class InvalidBIN(ValidationError):
    default_detail = _("Неверный БИН")
