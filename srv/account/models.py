from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractUser, UserManager
)
from django.contrib.auth.hashers import (
    check_password, make_password,
)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PasswordMixin(models.Model):
    password = models.CharField(_('password'), max_length=128)
    _password = None

    class Meta:
        abstract = True
        ordering = ('pk',)
        app_label = 'account'
        verbose_name = 'password'

    def __str__(self):
        return f'hashed password'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)


class User(AbstractUser):
    skku_id = models.CharField(verbose_name=_('SKKU ID'),
                               max_length=255,
                               null=True, blank=True)
    nickname = models.CharField(verbose_name=_('Nickname'),
                                max_length=255,
                                default=_('Amugae'))
    phone_num = models.CharField(verbose_name=_('Phone number'),
                                 max_length=255,
                                 null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'account'

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
