from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
import datetime
import dateparser

def validate_charfield(value):
    charfield_pattern = re.compile("^[A-Za-z\_]+$")
    if not charfield_pattern.match(value):
        raise ValidationError(
            _('%(value)s must have a valid format'),
            params={'value': value},
        )

def validate_id(value):
    id_pattern = re.compile("^[A-Za-z0-9\-]+$")
    if not id_pattern.match(value):
        raise ValidationError(
            _('%(value)s must have a valid format'),
            params={'value': value},
        )

def validate_date(value):
    datetime_value = value.split()
    date = ' '.join(datetime_value[0:len(datetime_value) - 1])
    try:
        datetime.datetime.strptime(date, '%H:%M:%S %b %d, %Y')
    except ValueError:
        raise ValidationError(
            _('%(value)s must have a valid format'),
            params={'value': value},
        )
