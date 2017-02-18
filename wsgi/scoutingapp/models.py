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
from django.core.validators import validate_comma_separated_integer_list

class Tournament(models.Model):
    name = models.CharField(max_length=200, default="UNAMED")

    def __str__(self):
        return self.name


class Team(models.Model):
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
        return str(self.team_number) + ": " + self.team_name


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

    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

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


class Card(models.Model):
    card_name = models.CharField(max_length=23)

    def __str__(self):
        return self.card_name

class HopperLoad(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class HighEfficiency(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class Match(models.Model):
    match_number = models.DecimalField(max_digits=100, decimal_places=0,
                                       default=0)
    scouted_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    auto_gears_scored = models.CharField(max_length=100)
    auto_move_yn = models.BooleanField(default=False, verbose_name="Moved on auto?")
    auto_score_gear_yn = models.BooleanField(default=False, verbose_name="Did it score on auto?")
    auto_low_goal = models.BooleanField(default=False)
    auto_trigger_hopper = models.DecimalField(default=0, max_digits=1,
                                              decimal_places=0, null=True)
    auto_hopper_load = models.ForeignKey(HopperLoad, null=True)
    auto_high_efficiency_load = models.ForeignKey(HighEfficiency,
                                                  related_name="auto_high_efficiency_load", null=True)
    auto_low_efficiency_load = models.ForeignKey(HighEfficiency, null=True)
    trigger_hopper = models.DecimalField(max_digits=1, decimal_places=0,
                                         default=0, null=True)
#     hopper_load = models.CharField(max_length=999
#                                    # validators=[validate_comma_separated_integer_list]
#                                    , null=True)
    

    gears_aquired = models.DecimalField(max_digits=1, decimal_places=0,
                                         default=0, null=True)
    gears_scored = models.DecimalField(max_digits=1, decimal_places=0,
                                         default=0, null=True)
    gears_picked_up = models.DecimalField(max_digits=1, decimal_places=0,
                                         default=0, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,
                                   null=True, blank=True)
    robot_end_game = models.ForeignKey(EndGameState,
                                     on_delete=models.CASCADE,
                                     related_name='robot1endgame',
                                     null=True)
    robot_card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True,
                                     related_name='Robot1card')
    scouted_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.match_number)


class Volley(models.Model):
    goal_type = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=100)
    ball_count = models.CharField(max_length=100)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    
class Gear(models.Model):
    source = models.CharField(max_length=100)
    dropped = models.CharField(max_length=100)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

class Alliance(models.Model):
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.color


class AllianceMatch(models.Model):
    match_number = models.DecimalField(max_digits=100, decimal_places=0,
                                       default=0)
    alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE)
    scouted_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    robot_1_driver_skill = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)
    robot_2_driver_skill = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)
    robot_3_driver_skill = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)
    robot_1_breach_ability = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)
    robot_2_breach_ability = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)
    robot_3_breach_ability = models.DecimalField(max_digits=10, decimal_places=0,
                                    default=0)

class CredentialsModel(models.Model):
    id = models.OneToOneField(MyUser, primary_key=True)
    credential = CredentialsField()

    def __str__(self):
        return str(self.id)


class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)
