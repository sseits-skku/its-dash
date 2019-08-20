from django.contrib.auth.models import AbstractUser, AbstractBaseUser, \
                                       UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AnonymousUser(AbstractBaseUser):
    nickname = models.CharField(verbose_name=_('Nickname'),
                                max_length=255,
                                default=_('Amugae'))
    phone = models.CharField(verbose_name=_('Phone number'),
                             max_length=255,
                             null=False)

    class Meta:
        app_label = 'account'
        ordering = ('nickname', 'phone')


class User(AnonymousUser, AbstractUser):
    objects = UserManager()

    class Meta:
        app_label = 'account'
