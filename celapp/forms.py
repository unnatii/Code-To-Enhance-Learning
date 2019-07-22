from django import forms
from django.contrib.auth.models import User
from .models import Profile,team
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
    role = forms.CharField(label='teacher or parent ', widget=forms.Select(choices=ROLES))

    def save(self, user_id, *args, **kwargs):
        self.instance.user_id = user_id
        return super(ProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('role','schoolname', 'contactname', 'phoneno')


GENDER=[('M', 'M'),
    ('F', 'F'), ]
EXPERTISE=[('Beginner','Beginner'),
 ('Intermediate','Intermediate'),('Advance','Advance')]

class TeamForm(forms.ModelForm):
    gender1= forms.CharField(label='Gender ', widget=forms.Select(choices=GENDER))
    gender2= forms.CharField(label='Gender ', widget=forms.Select(choices=GENDER))
    expertise1= forms.CharField(label='Expertise ', widget=forms.Select(choices=EXPERTISE))
    expertise2= forms.CharField(label='Expertise ', widget=forms.Select(choices=EXPERTISE))
    class Meta:
        model = team
        fields = ('student_name1','grade1', 'age1', 'gender1','expertise1','student_name2','grade2', 'age2', 'gender2','expertise2')

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
