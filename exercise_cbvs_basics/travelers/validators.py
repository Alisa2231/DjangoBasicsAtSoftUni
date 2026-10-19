from django.core.exceptions import ValidationError


def domain_validator(value):
    if not (value.endswith('university.com') or value.endswith('university.org')):
        raise ValidationError('Please enter a valid domain.')