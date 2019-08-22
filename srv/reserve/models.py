from django.db import models
from django.utils.translation import ugettext_lazy as _

from account.models import PasswordMixin
from utils.permissions import OwnerMixin
from utils.placeholder_models import PlaceholderModel, SharedCharField


class Room(PlaceholderModel):
    title = SharedCharField(vname='name',
                            unique=True,
                            null=False, blank=False)
    status = models.BooleanField(verbose_name=_('Room status'),
                                 default=True)
    capacity = models.IntegerField(verbose_name=_('Room capacity'),
                                   null=False)
    minimum = models.IntegerField(verbose_name=_('Room capacity'),
                                  null=False, default=1)

    class Meta:
        app_label = 'reserve'
        ordering = ('title', )
        verbose_name = _('room status')
        verbose_name_plural = _('room statuses')


class Seminar(PasswordMixin, OwnerMixin):
    room = models.ForeignKey('Room',
                             verbose_name=_('Which room'),
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    start_time = models.DateTimeField(verbose_name=_('Start time'),
                                      null=False)
    end_time = models.DateTimeField(verbose_name=_('End time'),
                                    null=False)
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)
    boss = models.ForeignKey('account.User',
                             verbose_name=_('Boss'),
                             related_name='boss',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    member = models.ManyToManyField('account.User',
                                    verbose_name=_('Members'),
                                    related_name='member',
                                    related_query_name='member',
                                    blank=True)
    # TODO: 상태: 승인, 반려, 확인필요 등이 있어야 함.

    class Meta:
        app_label = 'reserve'
        ordering = ('-start_time', '-end_time')
        verbose_name = _('seminar reservation')

    def __str__(self):
        return f'{self.room.title}: {self.start_time} ~ {self.end_time}'


class Card(PasswordMixin, OwnerMixin):
    # phone from AnonymousUser
    # name from AnonymousUser... although it is nickname ;(
    visit_time = models.DateTimeField(verbose_name=_('Visit time'),
                                      null=False)
    created_time = models.DateTimeField(
        verbose_name=_('Reservation submitted time'),
        null=False
    )
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)

    class Meta:
        app_label = 'reserve'
        ordering = ('-visit_time', )
        verbose_name = _('card reservation')
