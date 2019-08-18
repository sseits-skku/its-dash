from django.utils import timezone
from django.db import models


class ThingType(models.Model):
    title = models.CharField(max_length=255,
                             null=False)

    class Meta:
        app_label = 'thing'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.title


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

    class Meta:
        app_label = 'thing'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return ThingType.objects.get(pk=self.ttype_id).title


class Seat(models.Model):
    row = models.IntegerField(null=True)
    column = models.IntegerField(null=True)
    thing = models.ManyToManyField('Thing')

    class Meta:
        app_label = 'thing'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return f'row: {self.row}, column: {self.column}'
