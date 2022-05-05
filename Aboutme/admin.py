from django.contrib import admin
from . import models


@admin.register(models.AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'success_projects')


@admin.register(models.SocialMedia)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
