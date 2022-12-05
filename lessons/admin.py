from django.contrib import admin
from . import models
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','slug')

admin.site.register(models.LessonModels,LessonAdmin)