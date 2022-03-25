from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import UserManager


class UserTypes(models.TextChoices):
    USUAL = 'USUAL', 'Usual'


class User(AbstractBaseUser, PermissionsMixin):

    def get_owner(self):
        return self

    type = models.CharField(_('User type'), max_length=255, choices=UserTypes.choices, default=UserTypes.USUAL)

    first_name = models.CharField(_('First name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Last name'), max_length=255, null=True, blank=True)
    email = models.EmailField(_('Email'), unique=True)

    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, null=True)
    is_active = models.BooleanField(_('Active'), default=False)
    is_superuser = models.BooleanField(_('Is Admin'), default=False)
    is_staff = models.BooleanField(_('Staff user'), default=False)

    email_is_verified = models.BooleanField(_('Email is verified'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
