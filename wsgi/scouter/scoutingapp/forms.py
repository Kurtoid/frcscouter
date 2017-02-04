"""
this module handles how forms are generated and sent to views
"""
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django import forms
from scoutingapp.models import (MyUser, Match, Defense, Tournament,
                                Team, AllianceMatch, EndGameState)


class SortViewMatchForm(forms.Form):
    tourney_select = forms.ModelMultipleChoiceField(
        queryset=Tournament.objects.all(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super(SortViewMatchForm, self).__init__(*args, **kwargs)
        self.fields['tourney_select'].required = False


class MatchViewFormMetaOptions(forms.Form):
    show_defense_count = forms.NullBooleanField(initial=True,
                                                widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(MatchViewFormMetaOptions, self).__init__(*args, **kwargs)


class MatchNumberAttribs(forms.Form):
    scouted_team = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super(MatchNumberAttribs, self).__init__(*args, **kwargs)
        self.fields['scouted_team'].required = False
        self.fields['crossed_def'].required = False


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
    initial = {'robot_end_game': EndGameState.objects.get(state="Missed" +
                                                          " End Game")}

    class Meta:
        def getSelect(min, max):
            return forms.Select(choices=[(x,x) for x in range (min, max)])

        """ controls which model and fields are displayed """
        model = Match
        exclude = ['scouted_by', 'field_setup', 'tournament']
        widgets = {'auto_trigger_hopper': getSelect(0,6),
                   'trigger_hopper': getSelect(0,6),
                   'gears_aquired': getSelect(1,14),
                   'gears_scored': getSelect(1,14)}



    def __init__(self, *args, **kwargs):
        super(ScoutingForm, self).__init__(*args, **kwargs)
        self.fields['robot_card'].required = False
        #self.fields['tournament'].required = False
        """
        self.fields['defense1_crossed'].widget = forms.NumberInput(attrs={'class': 'col s6', })
        self.fields['defense2_crossed'].widget = forms.NumberInput(attrs={'class': 'col s6', })
        self.fields['defense3_crossed'].widget = forms.NumberInput(attrs={'class': 'col s6', })
        self.fields['defense4_crossed'].widget = forms.NumberInput(attrs={'class': 'col s6', })
        self.fields['defense5_crossed'].widget = forms.NumberInput(attrs={'class': 'col s6', })
        """

    def clean(self):
        print("clean called")
        cleaned_data = super(ScoutingForm, self).clean()
        match_num = cleaned_data.get("match_number")
        if match_num < 1:
            raise forms.ValidationError("Match must be more than 0!!")
        return cleaned_data


class AllianceScoutingForm(ModelForm):
    """ generates the scouting form """
    class Meta:
        """ controls which model and fields are displayed """
        model = AllianceMatch
        exclude = ['scouted_by', 'field_setup']

    def __init__(self, *args, **kwargs):
        super(AllianceScoutingForm, self).__init__(*args, **kwargs)

    def clean(self):
        print("clean called")
        cleaned_data = super(ScoutingForm, self).clean()
        match_num = cleaned_data.get("match_number")
        if match_num < 1:
            raise forms.ValidationError("Match must be more than 0!!")
        return cleaned_data


class UserControlForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['team']



class importTeamForm(forms.Form):
    team_number_begin = forms.IntegerField()
    team_number_end= forms.IntegerField()


class importEventForm(forms.Form):
    event_code = forms.CharField()
