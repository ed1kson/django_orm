import os
import django

os.environ.setdefault(key=("DJANGO_SETTINGS_MODULE"), value=("django_orm.settings"))
django.setup()
