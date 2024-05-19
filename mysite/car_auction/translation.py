from modeltranslation.translator import TranslationOptions, register
from .models import *


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ("car_name", "category", "city", "country", "description")
