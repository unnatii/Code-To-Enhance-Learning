from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# ROLES= [
#     ('teacher', ' Teacher'),
#     ('parent', 'Parent'),
#     ]


# class UserRegisterForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput)
#     email =forms.EmailField()
#     role= forms.CharField(label='Teacher or Parent ?', widget=forms.Select(choices=ROLES))
#
#     class Meta:
#         model = User
#         fields =['username',  'role',
#             'schoolname',
#             'contactname',
#             'phoneno',
#             'email',
#             'password1',
#             'password2']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'role',
            'schoolname',
            'contactname',
            'phoneno',
            'email',
            'password1',
            'password2'
        )

