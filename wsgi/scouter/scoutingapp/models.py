from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class Team(models.Model):
    team_number = models.DecimalField(max_digits=5, decimal_places=0,
                                      default=0000, primary_key=True)
    team_name = models.CharField(max_length=200, default="UNNAMED")

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

    def __str__(self):              # __unicode__ on Python 2
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


class Defense(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code + ": " + self.name


class FieldSetup(models.Model):
    defense1 = models.ForeignKey(Defense, related_name="Defense_1",
                                 on_delete=models.CASCADE)
    defense2 = models.ForeignKey(Defense, related_name="Defense_2", on_delete=models.CASCADE)
    defense3 = models.ForeignKey(Defense, related_name="Defense_3", on_delete=models.CASCADE)
    defense4 = models.ForeignKey(Defense, related_name="Defense_4", on_delete=models.CASCADE)
    defense5 = models.ForeignKey(Defense, related_name="Defense_5", on_delete=models.CASCADE)

    def __str__(self):
        result = self.defense1.name + " "
        result = result + self.defense2.name + " "
        result = result + self.defense3.name + " "
        result = result + self.defense4.name + " "
        result = result + self.defense5.name + " "
        return result



class Match(models.Model):
    match_number = models.DecimalField(max_digits=100, decimal_places=0,
                                       default=0)
    field_setup = models.OneToOneField(FieldSetup, on_delete=models.CASCADE)
    scouted_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    scouted_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    crossed_defense_on_auto = models.BooleanField(default=False)
    auto_defense_crossed = models.DecimalField(max_digits=1, decimal_places=0,
                                               default=False )
    auto_balls = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    high_balls = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    low_balls = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    score = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    did_loops = models.DecimalField(max_digits=100, decimal_places=0,
                                    default=0)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.match_number)