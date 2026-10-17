from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def validate_price(value):
#     if value <= 0:
#         raise ValidationError('Price must be greater than 0')

@deconstructible
class ValidatePrice:
    def __call__(self, value):
        if value <= 0:
            raise ValidationError('Price must be greater than 0')