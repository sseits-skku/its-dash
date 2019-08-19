from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, is_password_usable

from utils.mod_str import trunc


class Comment(models.Model):
    nickname = models.CharField(max_length=255,
                                null=False)
    ip_addr = models.CharField(max_length=15,
                               null=False)
    deleted = models.BooleanField(default=False)
    content = models.TextField(null=False)
    passwd = models.CharField(max_length=255,
                              null=False)
    is_subcomment = models.BooleanField(default=False)
    subcomment = models.ForeignKey('self',
                                   on_delete=models.CASCADE,
                                   null=True)
    
    class Meta:
        app_label = 'board'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return trunc(self.content, 20)


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)

    class Meta:
        app_label = 'board'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return trunc(self.title, 20)


class Tag(models.Model):
    title = models.CharField(max_length=255, null=False)

    class Meta:
        app_label = 'board'

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return trunc(self.title, 20)


class Post(models.Model):
    STATUS_TYPE = [
        ('NEW', '아직 읽지 않음'),
        ('ASSIGNED', '관리자가 인지함'),
        ('ACCEPTED', '관리자가 해결 중'),
        ('FIXED', '해결됨'),
        ('WONTFIX', '해결하지 않을 것'),
        ('DUPLICATED', '중복된 요청'),
    ]
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(max_length=255, null=False)
    passwd = models.CharField(max_length=255, null=False)
    deleted = models.BooleanField(default=False)
    ip_addr = models.CharField(max_length=15, null=False)
    nickname = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255,
                              choices=STATUS_TYPE,
                              default='NEW')
    created_date = models.DateTimeField(null=False,
                                        default=timezone.now)
    modified_date = models.DateTimeField(null=False,
                                         default=timezone.now)
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT)
    tag = models.ManyToManyField('Tag')
    comment = models.ForeignKey('Comment',
                                on_delete=models.CASCADE)

    class Meta:
        app_label = 'board'

    def __str__(self):
        return trunc(self.title, 20)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()


@receiver(pre_save, sender=Post)
@receiver(pre_save, sender=Comment)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.passwd):
        instance.passwd = make_password(instance.passwd)
