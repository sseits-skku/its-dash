from random import randint, choice
from datetime import datetime as dt

from lorem import sentence, paragraph
from names import get_first_name


def _eval_batch(num, func, ev, *args):
    if num > 1:
        ret = []
        for i in range(num):
            ret.append(func(*map(lambda a: ev(*a), args)))
        return tuple(ret)
    elif num == 1:
        return func(*args)
    else:
        raise ValueError('num should be more than 1.')


def _batch(num, func, *args):
    if num > 1:
        ret = []
        for i in range(num):
            ret.append(func(*args))
        return tuple(ret)
    elif num == 1:
        return func(*args)
    else:
        raise ValueError('num should be more than 1.')


def email(num):
    return _eval_batch(num,
                       lambda a, b, c: f'{a}@\
                                         {b}.\
                                         {c}',
                       choice,
                       ('kwon', 'kim', 'ryu'),
                       ('google', 'daum', 'naver'),
                       ('com', 'org', 'net'))


def boolean(num):
    return _batch(num,
                  choice,
                  (True, False))


def datetime(num):
    return _batch(num,
                  lambda a, b, c, d, e, f, g: dt(a, b, c,
                                                 d, e, f),
                  randint,
                  (1, 9999),
                  (1, 12),
                  (1, 28),
                  (0, 23),
                  (0, 59),
                  (0, 59),
                  (0, 999999))


def enum(num, e):
    return _batch(num,
                  choice,
                  e)


def content(num):
    return _batch(num,
                  paragraph)


def title(num):
    return _batch(num,
                  sentence)


def passwd(num):
    return _eval_batch(num,
                       lambda a: a[:15],
                       sentence,
                       '')


def phone_num(num):
    return _eval_batch(num,
                       lambda a: f'010{a:0<8}',
                       randint,
                       (0, 99999999))


def ip_addr(num):
    return _eval_batch(num,
                       lambda a, b, c, d: f'{a}.{b}.{c}.{d}',
                       randint,
                       (0, 255),
                       (0, 255),
                       (0, 255),
                       (0, 255))


def skku_id(num):
    return _batch(num,
                  randint,
                  1000000000,
                  9999999999)


def nickname(num):
    return _batch(num,
                  get_first_name)
