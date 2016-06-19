"""
this module handles how forms are generated and sent to views
"""
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django import forms
from scoutingapp.models import MyUser, Match, FieldSetup


class FieldSetupForm(ModelForm):
    """ form for field layout """

    class Meta:
        """ controls which model and fields are displayed """
        model = FieldSetup
        exclude = ['defense1']


class SignUpForm(ModelForm):
    """ handles generation of the sign up form """
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       max_length=100)

    class Meta:
        """ controls which model and fields are displayed """
        model = MyUser
        fields = ['email', 'team']

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords dont match!")
        return cleaned_data

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """ generates form for login screen """
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("invalid login")
        print("clean called: login done")
        return self.cleaned_data

    def getuser(self):
        """ returns user from login form; called from view """
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user


class ScoutingForm(ModelForm):
    """ generates the scouting form """
    class Meta:
        """ controls which model and fields are displayed """
        model = Match
        exclude = ['scouted_by', 'field_setup']

    def __init__(self, *args, **kwargs):
        super(ScoutingForm, self).__init__(*args, **kwargs)
        self.fields['auto_defense_crossed'].required = False