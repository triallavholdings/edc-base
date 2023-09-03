from datetime import timedelta

from django.core.exceptions import ValidationError

from ..utils import get_utcnow


def datetime_not_future(utc_datetime):
    time_error = timedelta(minutes=10)
    if utc_datetime > get_utcnow() + time_error:
        raise ValidationError('Cannot be a future date/time')


def date_not_future(value):
    if value > get_utcnow().date():
        raise ValidationError('Cannot be a future date')


def datetime_is_future(utc_datetime):
    time_error = timedelta(minutes=10)
    if utc_datetime < get_utcnow() + time_error:
        raise ValidationError('Expected a future date/time')


def date_is_future(value):
    if value < get_utcnow().date():
        raise ValidationError('Expected a future date')
