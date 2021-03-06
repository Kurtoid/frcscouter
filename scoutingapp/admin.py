"""
admin control settings
"""
import sys;
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.widgets import TextInput

from scoutingapp.models import (MyUser, Team, Match,
                                Tournament, Alliance, AllianceMatch,
                                EndGameState, Card, DetailUser, CubeWhen, CubePlace, CubeScored, CubeAcquired, ScheduledMatch)

class DefenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class TeamCreateForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('team_name', 'team_number', 'team_color', 'currently_in_event')
        widgets = {
            'team_color': TextInput(attrs={'type': 'color'}),
        }
        def __init__(self, *args, **kwargs):
            super(TeamCreateForm, self).__init__(*args, **kwargs)
            self.fields['team_color'].required=False;
            self.fields['currently_in_event'].required=False;




class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_number', 'team_name')
    form = TeamCreateForm


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'team', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin', 'team', 'first_name', 'last_name')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    raw_id_fields = ("team",)
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin', 'team_name', 'first_name')

    def team_name(self, obj):
        if(obj.team):
            return obj.team.team_name or ""
        else:
            return "none"
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Team', {'fields': ('team',)}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Name', {'fields': ('first_name', 'last_name')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'team')
        }),
    )
    search_fields = ('email', 'team')
    ordering = ('email', 'team')
    filter_horizontal = ()


class MatchAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'scouted_by':
            kwargs['initial'] = request.user.id
        return super(MatchAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
    list_display = ('match_number', 'scouted_team', 'scouted_by', 'created_at')
    list_per_page = sys.maxsize;

class DetailUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournament)
admin.site.register(Alliance)
admin.site.register(AllianceMatch)
admin.site.register(EndGameState)
admin.site.register(Card)
admin.site.register(CubePlace)
admin.site.register(CubeAcquired)
admin.site.register(CubeWhen)
admin.site.register(CubeScored)
admin.site.register(ScheduledMatch)
admin.site.register(DetailUser, DetailUserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
