# Custom settings for Rizoma overwrites

from .shared import *
from .env import (env, BASE_DIR)

LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/Lisbon"

# we need to add our rizoma app
INSTALLED_APPS.append("tapir.rizoma")

PHONENUMBER_DEFAULT_REGION = "PT"

ACTIVE_LOGIN_BACKEND = env.str("ACTIVE_LOGIN_BACKEND", default="coops.pt")
if ACTIVE_LOGIN_BACKEND == LOGIN_BACKEND_COOPS_PT:
    AUTHENTICATION_BACKENDS = ["tapir.rizoma.coops_pt_auth_backend.CoopsPtAuthBackend"]
    COOPS_PT_API_BASE_URL = env.str("COOPS_PT_API_BASE_URL", default="https://api.demo.coops.pt")
    COOPS_PT_API_KEY = env.str("COOPS_PT_API_KEY", default="invalid_key")
    COOPS_PT_RSA_PUBLIC_KEY_FILE_PATH = env.str("COOPS_PT_RSA_PUBLIC_KEY_FILE_PATH", default="")

# we prefix all templates with our custom rizoma templates
TEMPLATES[0]['DIRS'].insert(0, os.path.join(BASE_DIR, "rizoma/templates"))

# we have to upadte the celery background jobs to sync our users
CELERY_BEAT_SCHEDULE.update(
    {
        "sync_users_with_coops_pt_backend": {
            "task": "tapir.rizoma.tasks.sync_users_with_coops_pt_backend",
            "schedule": celery.schedules.crontab(hour="*", minute="0"),
        },
    }
)
