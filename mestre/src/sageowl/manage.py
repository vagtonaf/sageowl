#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import settings
except ImportError:
    import sys
    sys.stderr.write("Error: Nao pode encontrar o arquivo 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
