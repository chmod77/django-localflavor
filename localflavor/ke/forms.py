"""
Kenya-specific Form Helpers
"""
import re
from datetime import date
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import gettext_lazy as _


class KEPostalCodeField(RegexField):
    """
    A form field that validates input as a Kenyan Postal Code

    Valid Formats are AAAAAA, AAAA-AAAAA

    Example: 133 or 133-30200


    """

class KENationalIDField(CharField):...

class KEHudumaNumberField(CharField):...

class KEPassPortField(CharField):...



class KECountySelect(Select):...