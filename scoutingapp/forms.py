"""
this module handles how forms are generated and sent to views
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django import forms
from scoutingapp.models import (MyUser, Match, Tournament,
                                Team, AllianceMatch, EndGameState, DetailUser, CubePlace)
from django.utils.safestring import mark_safe

class CubePlaceForm(forms.ModelForm):
    class Meta:
        model = CubePlace
        fields = ['acquired', 'scored', 'when']
    def __init__(self, *args, **kwargs):
        super(CubePlaceForm, self).__init__(*args, **kwargs)
        self.fields['acquired'].required = False
        self.fields['scored'].required = False
        self.fields['when'].required = False

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


class SignUpForm(ModelForm):
    """ handles generation of the sign up form """
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       max_length=100)

    class Meta:
        """ controls which model and fields are displayed """
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'team']

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
    cube_placeholder = forms.CharField(label= "cubeplace", required = False)
    filterteams = forms.BooleanField(label = "Filter teams?", initial = True, required = False)
    # try:
        # initial = {'robot_end_game': EndGameState.objects.get(state="Missed Game")}
    # except ObjectDoesNotExist:
            # print("Missed game missing")

    class Meta:
        help_texts = {
        }
        def getSelect(min, max):  # @NoSelf
            return forms.Select(choices=[(x, x) for x in range (min, max)])

        """ controls which model and fields are displayed """
        model = Match
        exclude = ['scouted_by', 'field_setup', 'tournament', 'duplicate']
        widgets = {
            }
        fields = (
            'match_number',
            'filterteams',
             'scouted_team', 'auto_move_yn', 'cube_placeholder', 'robot_end_game', 'robot_card',
            )



    def __init__(self, *args, **kwargs):
        super(ScoutingForm, self).__init__(*args, **kwargs)
        self.fields['robot_card'].required = False
        self.fields['robot_end_game'].required = False
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
        def getSelect(min, max):  # @NoSelf
            return forms.Select(choices=[(x, x) for x in range (min, max)])
        """ controls which model and fields are displayed """
        model = AllianceMatch
        exclude = ['scouted_by', 'tournament', 'match_number', 'alliance', 'scouter_number']
        widgets = {
#             'auto_pilot_gears_acquired': getSelect(0, 4),
#             'auto_pilot_rotors_engaged': getSelect(0, 3),
#             'pilot_gears_acquired': getSelect(0, 14),
#             'pilot_rotors_engaged': getSelect(0, 5),
            }

    def __init__(self, *args, **kwargs):
        super(AllianceScoutingForm, self).__init__(*args, **kwargs)
        self.fields['robot_card'].required = False

    def clean(self):
        print("clean called")
        cleaned_data = super(AllianceScoutingForm, self).clean()
        match_num = cleaned_data.get("match_number")
        if match_num:
            if match_num < 1:
                raise forms.ValidationError("Match must be more than 0!!")
        return cleaned_data


class AlliancePreForm(ModelForm):
    class Meta:
        model = AllianceMatch
        fields = ['match_number', 'alliance']


class UserControlForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['team']



class importTeamForm(forms.Form):
    team_number_begin = forms.IntegerField()
    team_number_end = forms.IntegerField()


class importEventForm(forms.Form):
    event_code = forms.CharField()

class openHouseForm(ModelForm):
    class Meta:
        model = DetailUser
        exclude = []
