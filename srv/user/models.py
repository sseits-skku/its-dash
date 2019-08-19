from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, is_password_usable


class Person(models.Model):
    skku_id = models.CharField(max_length=80, unique=True, null=False)
    username = models.CharField(max_length=80, unique=True, null=False)

    
    class Meta:
        app_label = 'user'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return f'ID: {self.skku_id}, NAME: {self.username}'


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

    class Meta:
        app_label = 'user'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        t = self.nickname
        if not t:
            return Person.objects.get(pk=self.person).username
        return t


@receiver(pre_save, sender=Member)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.passwd):
        instance.passwd = make_password(instance.passwd)
