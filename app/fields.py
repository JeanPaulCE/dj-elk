from django.forms.widgets import EmailInput, NumberInput, PasswordInput


class EEmailInput(EmailInput):

    def __init__(self, attrs={}):
        attrs.update({
            'class': 'form-input',
        })
        super().__init__(attrs=attrs)
