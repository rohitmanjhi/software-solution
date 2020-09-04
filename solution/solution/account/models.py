from django.db import models
from django.core.mail import send_mail
# import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length=88, blank=True)
    email = models.EmailField(
        _('email address'), unique=True, null=True)
    mobile = models.CharField(unique=True, max_length=100)

    USERNAME_FIELD = 'email'
