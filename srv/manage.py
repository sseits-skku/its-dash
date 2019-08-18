#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    if '--dev' in sys.argv:
        sys.argv.remove('--dev')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'server.settings.development')
    elif '--prod' in sys.argv:
        sys.argv.remove('--prod')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'server.settings.production')
    elif '--test' in sys.argv:
        sys.argv.remove('--test')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'server.settings.test')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'server.settings.development')
        '''
        raise ValueError(
            "\nPlease Specify environment. \n"
            "\'--dev\' for develoment, \n"
            "\'--prod\' for production, \n"
            "\'--test\' for test."
        )
        '''
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
