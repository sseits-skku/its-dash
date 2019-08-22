from importlib import import_module

from django.core.management import BaseCommand

from account.models import User
from board.models import Tag, Post, Comment, Category, \
                         PostStatus
from inventory.models import Stock, OSType, Computer,  \
                             StockType, StockStatus
from iptable.models import IPAddress
from reserve.models import Card, Room, Seminar
from utils.generate_random import RandomGenerator


class Command(BaseCommand):
    help = 'Generate Testsets.'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)
        parser.add_argument(
            '-r', '--random',
            action='store_true',
            help='Generate random content'
        )
        parser.add_argument(
            '-n', '--numpy',
            action='store_true',
            help='Use numpy.random instead of native one.'
        )
    
    def handle(self, *args, **options):
        num = options.get('num')
        if not num or num <= 0:
            raise ValueError('Invalid arguments...')
        random = RandomGenerator(num)
        '''
        if '-n' in options or '--numpy' in options:
            random = import_module('numpy.random')
        if '-r' not in options and '--random' not in options:
            random = import_module('random')
        '''
        for i in range(num):
            User
            Tag
            Post
            Comment
            Category
            PostStatus
            Stock
            OSType
            Computer
            StockType
            StockStatus
            IPAddress
            Card
            Room
            Seminar
