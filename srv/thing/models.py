from django.utils import timezone
from django.db import models


class ThingType(models.Model):
    title = models.CharField(max_length=255,
                             null=False)


class Thing(models.Model):
    supply_id = models.CharField(max_length=255,
                                 null=False)
    discarded = models.BooleanField(default=False)
    broken = models.BooleanField(default=False)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(
                          null=False,
                          default=timezone.now)
    discarded_date = models.DateTimeField(
                            null=True)
    ttype_id = models.ForeignKey('ThingType',
                                 on_delete=models.PROTECT)


class Seat(models.Model):
    row = models.IntegerField(null=True)
    column = models.IntegerField(null=True)
    thing = models.ManyToManyField('Thing')
