from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.contrib.django_util.models import CredentialsField
from django.core.validators import validate_comma_separated_integer_list,\
    MaxValueValidator, MinValueValidator
from unittest.util import _MAX_LENGTH

class Tournament(models.Model):
    name = models.CharField(max_length=200, default="UNAMED")
    event_code = models.CharField(max_length=200, default="UNAMED")

    def __str__(self):
        return self.name


class Team(models.Model):
    currently_in_event = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    team_number = models.DecimalField(max_digits=5, decimal_places=0,
                                      default=0000, primary_key=True)
    team_name = models.CharField(max_length=200, default="UNNAMED")

    team_color = models.CharField(max_length=7, null=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ("team_number",)

    def get_full_name(self):
        return self.team_name

    def get_short_name(self):
        return self.team_name

    def __str__(self):
        return str(self.team_number or "") + ": " + self.team_name or ""


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        creates and saves a user
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email
        and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    first_name = models.CharField(max_length= 100, default = "", null=True)
    last_name = models.CharField(max_length=100, null = True, default = "")

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name + " " + self.last_name + " (" + str(self.team.team_number or "") + ")"


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class EndGameState(models.Model):
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state

class PreloadedGearAction(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['updated_at']


class Card(models.Model):
    card_name = models.CharField(max_length=23)

    def __str__(self):
        return self.card_name


class Match(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    match_number = models.DecimalField(max_digits=100, decimal_places=0,
                                       default=0)
    scouted_team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     auto_gears_scored = models.CharField(max_length=100)
    auto_move_yn = models.BooleanField(default=False, verbose_name="Auto Move")
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL,
                                   null=True, blank=True)
    robot_end_game = models.ForeignKey(EndGameState,
                                     on_delete=models.SET_NULL,
                                     related_name='robot1endgame',
                                     null=True)
    robot_card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='Robot1card')
    scouted_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    duplicate = models.DecimalField(max_digits=100, decimal_places=0, null=True)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.match_number)

class CubeAcquired(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.name

class CubeScored(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    def __str__(self):
        return self.name

class CubeWhen(models.Model):
    name = models.CharField(max_length = 50, unique= True)
    def __str__(self):
        return self.name

class CubePlace(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    acquired = models.ForeignKey(CubeAcquired, on_delete = models.CASCADE)
    scored = models.ForeignKey(CubeScored, on_delete=models.CASCADE)
    when = models.ForeignKey(CubeWhen, on_delete = models.CASCADE)


class Alliance(models.Model):
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.color

class AllianceMatch(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL,
                                   null=True, blank=True)
    match_number = models.DecimalField(max_digits=100, decimal_places=0,
                                       default=0)
    alliance = models.ForeignKey(Alliance)
    scouter_number = models.DecimalField(max_digits=1, decimal_places=0)
    scouted_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    robot_card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='pilot1card')

class CredentialsModel(models.Model):
    id = models.OneToOneField(MyUser, primary_key=True)
    credential = CredentialsField()

    def __str__(self):
        return str(self.id)


class CredentialsAdmin(admin.ModelAdmin):
    pass

class DetailUser(models.Model):
    first_name = models.CharField(max_length= 100, default = "", null=True)
    last_name = models.CharField(max_length=100, null = True, default = "")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(max_length=15)



admin.site.register(CredentialsModel, CredentialsAdmin)
