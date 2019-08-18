from django.db import models


class Person(models.Model):
    skku_id = models.CharField(max_length=80, unique=True, null=False)
    username = models.CharField(max_length=80, unique=True, null=False)


class Member(models.Model):
    login_id = models.CharField(max_length=255,
                                unique=True, null=False)
    passwd = models.CharField(max_length=255,
                              null=False)
    nickname = models.CharField(max_length=255,
                                null=True)
    email = models.CharField(max_length=255,
                             null=False)
    phone = models.CharField(max_length=255,
                             null=False)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    person = models.ForeignKey('Person',
                               on_delete=models.PROTECT)
