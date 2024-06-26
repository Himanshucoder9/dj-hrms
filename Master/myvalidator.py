from django.core import validators
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


phone_regex = RegexValidator(
    regex=r"^989\d{2}\s*?\d{3}\s*?\d{4}$", message="Invalid phone number.",
)
mobile_validator = RegexValidator(
        regex=r'^\+\d{1,13}$',
        message='Mobile number must be in the format "+911234567890".',
        code='invalid_mobile_format'
    )
    
# phone_regex = RegexValidator(
#     regex=r"^989\d{2}\s*?\d{3}\s*?\d{4}$", message="Invalid phone number.",
# )


def alphanumeric(msg):
    alpha = validators.RegexValidator(r'^[a-zA-Z0-9\s]*$', message=f"{msg} must be Alphanumeric!!!")
    return alpha


def minimum(length, msg):
    minlen = validators.MinLengthValidator(
        length, f"{msg} must be have at least {length} digits!!!")
    return minlen


def maximum(length, msg):
    maxlen = validators.MaxLengthValidator(
        length, f"{msg} must be {length} digits!!!")
    return maxlen


def alphabet(msg):
    aerror = validators.RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message=f"{msg} must be Alphabet!!!")
    return aerror


def numeric(msg):
    nerror = validators.RegexValidator(
        r'^[0-9]*$', message=f"{msg} must be number!!!")
    return nerror


def pan_validator(value):
    pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
    if not pattern.match(str(value)):
        raise ValidationError(
            _('Enter a valid PAN card number. Example: ABCDE1234F'),
            code='invalid_pan_number'
        )