from django.contrib import admin
from .models import Class

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'class_name',
        'class_time',
        'class_type',
        'class_level',
    )

    ordering = ('class_name',)


admin.site.register(Class, ClassAdmin)
