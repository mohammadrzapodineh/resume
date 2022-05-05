from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.core.validators import EmailValidator, MaxLengthValidator
from django.conf import settings

error_messages = {
    'required': 'این فیلد اجباری است  '
}


class ContactForm(forms.Form):
    name = forms.CharField(error_messages=error_messages,
                           widget=forms.TextInput(
                            attrs={'class': 'form-control',  'placeholder': "نام شما *"}
        ), validators=[MaxLengthValidator(110, message='کارکتر های مجاز 110 تا میباشد')]
    )

    email = forms.CharField(error_messages=error_messages,
                            widget=forms.EmailInput(
                            attrs={'class': 'form-control', 'placeholder': "ایمیل شما *"}
        ),                 validators=[EmailValidator(message='ایمیل وارد شده صحیح نیست')]
    )

    text = forms.CharField(error_messages=error_messages,
                           widget=forms.Textarea(
                            attrs={'class': 'form-control', 'placeholder': "متن  *"}
        )
    )

    captcha = ReCaptchaField(error_messages=error_messages, public_key=settings.RECAPTCHA_PUBLIC_KEY
                             , private_key=settings.RECAPTCHA_PRIVATE_KEY,
                             widget=ReCaptchaV3(api_params={'hl': 'fa'})
    )
