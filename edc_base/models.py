from django.conf import settings

from .auth.models import UserProfile

if settings.APP_NAME == 'edc_base':
    from .tests.models import TestModel, TestValidatorModel
