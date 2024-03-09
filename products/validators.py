from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# def validate_title(value):
#     is_exist = Product.objects.filter(title__iexact=value).exists()
#     if is_exist:
#         raise serializers.ValidationError(f"{value} is aleady a product name")
#     else:
#         return value


def no_hi_in_title(value):
    if "hi" in value:
        raise serializers.ValidationError('Hi is not allowed in title')
    else:
        return value
    
title_unique_validator=UniqueValidator(Product.objects.all())