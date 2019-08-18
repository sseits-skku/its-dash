from django.utils import timezone
from django.db import models


STATUS_TYPE = [
    ('NEW', '아직 읽지 않음'),
    ('ASSIGNED', '관리자가 인지함'),
    ('ACCEPTED', '관리자가 해결 중'),
    ('FIXED', '해결됨'),
    ('WONTFIX', '해결하지 않을 것'),
    ('DUPLICATED', '중복된 요청'),
]


ROOM_TYPE = [
    ('GREEN', '그린 (4인실)'),
    ('ORANGE', '오렌지 (10인실)'),
    ('YELLOW', '옐로우 (6인실)'),
    ('BLUE', '블루 (6인실)'),
]


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
    boss = models.OneToOneField('Person',
                                related_name='boss',
                                on_delete=models.SET_NULL,
                                null=True)
    friends = models.ForeignKey('Person',
                                related_name='friends',
                                on_delete=models.SET_NULL,
                                null=True)


class Card(models.Model):
    visit_date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(null=False,
                                        default=timezone.now)
    person = models.OneToOneField('Person',
                                  on_delete=models.SET_NULL,
                                  null=True)


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
