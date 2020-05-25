from django.contrib import admin

from .models import Sample

# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields': ['sample_title', 'sample_published']}),
        ('Content', {'fields': ['sample_content']})
    ]

admin.site.register(Sample, SampleAdmin)