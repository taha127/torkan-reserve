from django import forms
from kavenegar import KavenegarAPI

class PhoneNumberForm(forms.Form):
    class Meta:

        phone_number = forms.CharField(max_length=11,)


def send_verification_code(phone_number):
    api_key = '***REMOVED***'
    api = KavenegarAPI(api_key)
    params = {
        'receptor': phone_number,
        'template' : 'verifi'

    }
    response = api.sms_send(params)
    return response

class verificationCodeForm(forms.Form):

    verification_code = models.CharField(max_length=4, null=True, blank=True)