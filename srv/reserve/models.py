from django.utils import timezone
from django.db import models


ROOM_TYPE = [
    ('GREEN', '그린 (4인실)'),
    ('ORANGE', '오렌지 (10인실)'),
    ('YELLOW', '옐로우 (6인실)'),
    ('BLUE', '블루 (6인실)'),
]


class Seminar(models.Model):
    room = models.CharField(max_length=255,
                            choices=ROOM_TYPE,
                            null=False)
    phone = models.CharField(max_length=255,
                             null=False)
    start_time = models.DateTimeField(
                        null=False,
                        default=timezone.now)
    end_time = models.DateTimeField(
                      null=False,
                      default=timezone.now)
    boss = models.OneToOneField('user.Person',
                                related_name='boss',
                                on_delete=models.SET_NULL,
                                null=True)
    friends = models.ForeignKey('user.Person',
                                related_name='friends',
                                on_delete=models.SET_NULL,
                                null=True)


class Card(models.Model):
    visit_date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(null=False,
                                        default=timezone.now)
    person = models.OneToOneField('user.Person',
                                  on_delete=models.SET_NULL,
                                  null=True)
