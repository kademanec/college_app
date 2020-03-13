from django import forms
from collegeapp.models import Sign_up

class Sign_up(forms.ModelForm):
    class Meta:
        model = Sign_up
          widgets = {
        'password': forms.PasswordInput(),
    }
