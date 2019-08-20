from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import AnonymousUser
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
        verbose_name = _('post status')
        verbose_name_plural = _('post statuses')


class Seminar(AnonymousUser):
    room = models.ForeignKey('Room',
                             verbose_name=_('Which room'),
                             on_delete=models.SET_NULL,
                             null=True)
    # phone from AnonymousUser
    start_time = models.DateTimeField(verbose_name=_('Start time'),
                                      null=False)
    end_time = models.DateTimeField(verbose_name=_('End time'),
                                    null=False)
    # boss from AnonymousUser
    member = models.ManyToManyField('account.AnonymousUser',
                                    verbose_name=_('Members'),
                                    related_name='member',
                                    related_query_name='member')

    class Meta:
        app_label = 'reserve'
        ordering = ('-start_time', '-end_time')
        verbose_name = _('seminar reservation')

    def __repr__(self):
        return f'{self.room.title}: {self.start_time} ~ {self.end_time}'

    def __unicode__(self):
        return f'{self.room.title}: {self.start_time} ~ {self.end_time}'

    def __str__(self):
        return f'{self.room.title}: {self.start_time} ~ {self.end_time}'


class Card(AnonymousUser):
    # phone from AnonymousUser
    # name from AnonymousUser... although it is nickname ;(
    visit_time = models.DateTimeField(verbose_name=_('Visit time'),
                                      null=False)
    created_time = models.DateTimeField(
        verbose_name=_('Reservation submitted time'),
        null=False
    )

    class Meta:
        app_label = 'reserve'
        ordering = ('-visit_time', )
        verbose_name = _('card reservation')
