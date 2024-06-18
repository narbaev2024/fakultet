from django.contrib import admin
from .models import Course, Fakultet, Professor, Student, Sdacha_dz, Cabinet, Zapis_na_course, Dz, Raspisanie
from modeltranslation.admin import TranslationAdmin

@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ("name", "code", "department", "professor")
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Fakultet)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Sdacha_dz)
admin.site.register(Cabinet)
admin.site.register(Zapis_na_course)
admin.site.register(Dz)
admin.site.register(Raspisanie)
