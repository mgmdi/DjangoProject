from django import forms
import re
import datetime

class ValidatorForm(forms.Form):
    """
        Validate form: validates existence and general form of input
    """
    protection_eligibility = forms.CharField(max_length=50)
    address_status = forms.CharField(max_length=50)
    payer_id = forms.CharField(max_length=50)
    payment_date = forms.CharField()
    payment_status = forms.CharField(max_length=50)
    notify_version = forms.CharField(max_length=10)
    verify_sign = forms.CharField(max_length=60)
    receiver_id = forms.CharField(max_length=50)
    txn_type = forms.CharField(max_length=20)
    item_name = forms.CharField(max_length=20)
    mc_currency = forms.CharField(max_length=3)
    payment_gross = forms.FloatField()
    shipping = forms.FloatField()

    def clean(self):
        """
            Validation function: specific validations for each type of field

                Validate ids: only aphanumeric chars and divider (-), accepts XXXX-XXXXXX-XXXX

                Validate string fields: accepts XXXXXXX or XXXXX_XXXXX

                Validate date: valid date and format

        """

        # Fields 

        payer_id = self.cleaned_data['payer_id']

        verify_sign = self.cleaned_data['verify_sign']

        receiver_id = self.cleaned_data['receiver_id']

        protection_eligibility = self.cleaned_data['protection_eligibility']

        address_status = self.cleaned_data['address_status']

        payment_status = self.cleaned_data['payment_status']

        payment_date = self.cleaned_data['payment_date']

        txn_type = self.cleaned_data['txn_type']

        item_name = self.cleaned_data['item_name']

        # ID Validations

        if not validate_id(payer_id):
            raise forms.ValidationError('Payer ID must have a valid format')
        if not validate_id(receiver_id):
            raise forms.ValidationError('Receiver ID must have a valid format')
        if not validate_id(verify_sign):
            raise forms.ValidationError('Verify Sign must have a valid format')

        # Charfields Validations

        if not validate_charfield(protection_eligibility):
            raise forms.ValidationError('Proyection Eligibility must have a valid format')
        if not validate_charfield(address_status):
            raise forms.ValidationError('Address Status must have a valid format')
        if not validate_charfield(payment_status):
            raise forms.ValidationError('Payment Status must have a valid format')
        if not validate_charfield(txn_type):
            raise forms.ValidationError('Txn Type must have a valid format')
        if not validate_charfield(item_name):
            raise forms.ValidationError('Item Name must have a valid format')

        # Validate Date

        try:
            datetime.datetime.strptime(payment_date, '%H:%M:%S %b %d, %Y %Z')
        except ValueError:
            raise forms.ValidationError("Incorrect data format, should be H:M:S b d, YYYY Z")



def validate_charfield(field):
    charfield_pattern = re.compile("^[A-Za-z\_]+$")
    if not charfield_pattern.match(field):
        return False
    return True

def validate_id(field):
    id_pattern = re.compile("^[A-Za-z0-9\-]+$")
    if not id_pattern.match(field):
        return False
    return True


