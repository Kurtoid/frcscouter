"""
admin control settings
"""
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from scoutingapp.models import (MyUser, Team, Match, FieldSetup, Defense,
                                Tournament)


class DefenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('team_number', 'team_name')
        }),
    )
    list_display = ('team_number', 'team_name')


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'team')

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
        fields = ('email', 'password', 'is_active', 'is_admin', 'team')

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
    list_display = ('email', 'is_admin', 'team_name')

    def team_name(self, obj):
        return obj.team.team_name
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Team', {'fields': ('team',)}),
        ('Permissions', {'fields': ('is_admin',)}),
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
    list_display = ('match_number', 'scouted_team', 'scouted_by')


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Defense, DefenseAdmin)
admin.site.register(FieldSetup)
admin.site.register(Tournament)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
