from django.utils import timezone
from django.db import models


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
                                   on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)


class Tag(models.Model):
    title = models.CharField(max_length=255, null=False)


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