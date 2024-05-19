from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(CarMake)
admin.site.register(Model)
admin.site.register(Bet)
admin.site.register(Comment)


@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ("car_name", "category", "city", "country", "description")

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',)
        }
