from django import forms
from validator import validators

class ValidatorForm(forms.Form):
    """
        Validate form: validates existence and general form of input
    """
    protection_eligibility = forms.CharField(
        max_length=50,
        validators=[
            validators.validate_charfield
        ]
        )
    address_status = forms.CharField(
        max_length=50,
        validators=[
            validators.validate_charfield
        ]
        )
    payer_id = forms.CharField(
        max_length=50,
        validators=[
            validators.validate_id
        ]
        )
    payment_date = forms.CharField(
        validators=[
            validators.validate_date
        ]
    )
    payment_status = forms.CharField(
        max_length=50,
        validators=[
            validators.validate_charfield
        ]
        )
    notify_version = forms.CharField(
        max_length=10
        )
    verify_sign = forms.CharField(
        max_length=60,
        validators=[
            validators.validate_id
        ]
        )
    receiver_id = forms.CharField(
        max_length=50,
        validators=[
            validators.validate_id
        ]
        )
    txn_type = forms.CharField(
        max_length=20,
        validators=[
            validators.validate_charfield
        ]
        )
    item_name = forms.CharField(
        max_length=20,
        validators=[
            validators.validate_charfield
        ]
        )
    mc_currency = forms.CharField(
        max_length=3
        )
    payment_gross = forms.FloatField()
    shipping = forms.FloatField()



