from django.contrib import admin
from .models import WorkHistory, EducationHistory, Skill, Portfolio
from django.utils.html import  format_html


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'date')


@admin.register(EducationHistory)
class EducationHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'field_of_study', 'date')


@admin.register(Skill)
class EducationHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent', 'is_circle')


@admin.register(Portfolio)
class EducationHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_image_tag')

    def show_image_tag(self, obj):
        return format_html(f"<img src='{obj.image.url}' width='100' height='100' />")

    show_image_tag.short_description = 'تصویر نمونه کار'
    show_image_tag.allow_tags = True

