from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import Sample

# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields': ['sample_title', 'sample_published']}),
        ('Content', {'fields': ['sample_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Sample, SampleAdmin)