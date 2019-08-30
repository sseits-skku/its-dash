from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractUser, UserManager
)
from django.contrib.auth.hashers import (
    check_password, make_password,
)
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'account'
        ordering = ('-date_joined', )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.is_active = False
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()
