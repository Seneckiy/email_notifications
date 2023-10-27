# File sets up the django environment, used by other scripts that need to
# execute in django land
import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "email_notifications"))

def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        INSTALLED_APPS=(
            "email_notifications",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()