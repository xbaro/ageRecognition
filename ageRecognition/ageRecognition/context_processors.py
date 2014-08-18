from django.conf import settings


def app_version_proc(request):
    "A context processor that provides 'app_version'."
    return {
        'app_version': settings.AGE_RECOGNITION_VERSION,
        'last_commit': settings.AGE_RECOGNITION_LAST_COMMIT
    }
