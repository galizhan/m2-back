from django.core.exceptions import ValidationError
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _

from core.exceptions import InvalidIIN, InvalidBIN


def validate_identifier(identifier):
    if len(identifier) == 12 and identifier.isdigit():
        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        b2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]
        control = 0
        for i in range(11):
            control = (control + b1[i] * int(identifier[i])) % 11
        
        if control == 10:
            control = 0
            for i in range(11):
                control = (control + b2[i] * int(identifier[i])) % 11
        
        if control != 10:
            if control == int(identifier[11]):
                return True

    return False


def check_iin_birthday(string_6):
    try:
        datetime.strptime(string_6, '%y%m%d')
        return True
    except ValueError:
        return False


def validate_iin(identifier):
    if not validate_identifier(identifier) or not check_iin_birthday(identifier[:6]):
        raise InvalidIIN


def validate_bin(identifier):
    if not validate_identifier(identifier) or int(identifier[4]) not in [4, 5, 6]:
        raise InvalidBIN


def validate_postal_code(value):
    if not value.isdigit():
        raise ValidationError(
            _('%(value)s must be an integer'),
            params={'value': value},
        )
