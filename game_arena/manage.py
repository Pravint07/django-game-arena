#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyfightarena.settings')
    try:
        # Ensure Django is installed: pip install django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Make sure it is installed (pip install django).") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

