from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
#


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields +(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


ROLES= [
    ('Teacher', 'Teacher'),
    ('Parent', 'Parent'),

    ]
class ProfileForm(forms.ModelForm):
    role= forms.CharField(label='teacher or parent ', widget=forms.Select(choices=ROLES))
    class Meta:
        model = Profile
        fields = ('role','schoolname', 'contactname', 'phoneno')
        

# # ROLES= [
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


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'role',
#             'schoolname',
#             'contactname',
#             'phoneno',
#             'email',
#             'password1',
#             'password2'
#         )
#
