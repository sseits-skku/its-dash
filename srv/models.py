# coding: utf-8
from app.db import Boolean, Column, DateTime, ForeignKey, \
                   Index, Integer, Model, String, Text,   \
                   relationship


class Card(Model):
    __tablename__ = 'card'
    id = Column(Integer,
                primary_key=True)
    visit_date = Column(DateTime,
                        nullable=False)
    created_date = Column(DateTime,
                          nullable=False)
    person_id = Column(ForeignKey('person.id'))
    person = relationship(
        'Person',
        primaryjoin='Card.person_id == Person.id',
        backref='cards'
    )


class Category(Model):
    __tablename__ = 'category'

    id = Column(Integer,
                primary_key=True)
    title = Column(String(255),
                   nullable=False)

    def __init__(self):
        pass


class Comment(Model):
    __tablename__ = 'comment'

    id = Column(Integer,
                primary_key=True)
    nickname = Column(String(255),
                      nullable=False)
    ip_addr = Column(String(15),
                     nullable=False)
    deleted = Column(Boolean,
                     nullable=False)
    content = Column(Text,
                     nullable=False)
    passwd = Column(String(255),
                    nullable=False)
    is_subcomment = Column(Boolean,
                           nullable=False)
    subcomment_id = Column(
        ForeignKey('comment.id'),
        nullable=False,
        index=True
    )
    subcomment = relationship(
        'Comment',
        remote_side=[id],
        primaryjoin='Comment.subcomment_id == Comment.id',
        backref='comments'
    )

    def __init__(self):
        pass


class Member(Model):
    __tablename__ = 'member'

    id = Column(Integer,
                primary_key=True)
    login_id = Column(String(255),
                      nullable=False)
    passwd = Column(String(255),
                    nullable=False)
    nickname = Column(String(255))
    email = Column(String(255),
                   nullable=False)
    phone = Column(String(255),
                   nullable=False)
    active = Column(Boolean,
                    nullable=False)
    description = Column(Text)
    person_id = Column(ForeignKey('person.id'),
                       nullable=False,
                       index=True)

    person = relationship(
        'Person',
        primaryjoin='Member.person_id == Person.id',
        backref='members'
    )

    def __init__(self):
        pass


class Person(Model):
    __tablename__ = 'person'

    id = Column(Integer,
                primary_key=True)
    skku_id = Column(String(80),
                     nullable=False)
    username = Column(String(80),
                      nullable=False)

    def __init__(self):
        pass


class Post(Model):
    __tablename__ = 'post'

    id = Column(Integer,
                primary_key=True)
    title = Column(String(255),
                   nullable=False)
    content = Column(Text,
                     nullable=False)
    passwd = Column(String(255),
                    nullable=False)
    deleted = Column(Boolean,
                     nullable=False)
    ip_addr = Column(String(15),
                     nullable=False)
    nickname = Column(String(255),
                      nullable=False)
    status = Column(String(255),
                    nullable=False)
    created_date = Column(DateTime,
                          nullable=False)
    modified_date = Column(DateTime,
                           nullable=False)
    category_id = Column(
        ForeignKey('category.id'),
        nullable=False,
        index=True
    )
    comment_id = Column(
        ForeignKey('comment.id'),
        nullable=False,
        index=True
    )

    category = relationship(
        'Category',
        primaryjoin='Post.category_id == Category.id',
        backref='posts'
    )
    comment = relationship(
        'Comment',
        primaryjoin='Post.comment_id == Comment.id',
        backref='posts'
    )

    def __init__(self):
        pass


class PostTag(Model):
    __tablename__ = 'post_tag'
    __table_args__ = (
        Index('post_tag_post_id_tag_id_bc32fa95_uniq',
              'post_id',
              'tag_id'),
    )

    id = Column(Integer,
                primary_key=True)
    post_id = Column(ForeignKey('post.id'),
                     nullable=False,
                     index=True)
    tag_id = Column(ForeignKey('tag.id'),
                    nullable=False,
                    index=True)

    post = relationship(
        'Post',
        primaryjoin='PostTag.post_id == Post.id',
        backref='post_tags'
    )
    tag = relationship(
        'Tag',
        primaryjoin='PostTag.tag_id == Tag.id',
        backref='post_tags'
    )

    def __init__(self):
        pass


class Seat(Model):
    __tablename__ = 'seat'

    id = Column(Integer,
                primary_key=True)
    row = Column(Integer)
    column = Column(Integer)

    def __init__(self):
        pass


class SeatThing(Model):
    __tablename__ = 'seat_thing'
    __table_args__ = (
        Index('seat_thing_seat_id_thing_id_7e978bad_uniq',
              'seat_id',
              'thing_id'),
    )

    id = Column(Integer,
                primary_key=True)
    seat_id = Column(ForeignKey('seat.id'),
                     nullable=False,
                     index=True)
    thing_id = Column(ForeignKey('thing.id'),
                      nullable=False,
                      index=True)

    seat = relationship(
        'Seat',
        primaryjoin='SeatThing.seat_id == Seat.id',
        backref='seat_things'
    )
    thing = relationship(
        'Thing',
        primaryjoin='SeatThing.thing_id == Thing.id',
        backref='seat_things'
    )

    def __init__(self):
        pass


class Seminar(Model):
    __tablename__ = 'seminar'

    id = Column(Integer,
                primary_key=True)
    room = Column(String(255),
                  nullable=False)
    phone = Column(String(255),
                   nullable=False)
    start_time = Column(DateTime,
                        nullable=False)
    end_time = Column(DateTime,
                      nullable=False)
    boss_id = Column(ForeignKey('person.id'))
    friends_id = Column(ForeignKey('person.id'),
                        index=True)

    boss = relationship(
        'Person',
        primaryjoin='Seminar.boss_id == Person.id',
        backref='genperson_seminars'
    )
    friends = relationship(
        'Person',
        primaryjoin='Seminar.friends_id == Person.id',
        backref='genperson_seminars_0'
    )

    def __init__(self):
        pass


class Tag(Model):
    __tablename__ = 'tag'

    id = Column(Integer,
                primary_key=True)
    title = Column(String(255),
                   nullable=False)

    def __init__(self):
        pass


class Thing(Model):
    __tablename__ = 'thing'

    id = Column(Integer,
                primary_key=True)
    supply_id = Column(String(255),
                       nullable=False)
    discarded = Column(Boolean,
                       nullable=False)
    broken = Column(Boolean,
                    nullable=False)
    description = Column(Text)
    created_date = Column(DateTime,
                          nullable=False)
    discarded_date = Column(DateTime)
    ttype_id_id = Column(ForeignKey('thingtype.id'),
                         nullable=False,
                         index=True)

    ttype_id = relationship(
        'Thingtype',
        primaryjoin='Thing.ttype_id_id == Thingtype.id',
        backref='things'
    )

    def __init__(self):
        pass


class Thingtype(Model):
    __tablename__ = 'thingtype'

    id = Column(Integer,
                primary_key=True)
    title = Column(String(255),
                   nullable=False)

    def __init__(self):
        pass
