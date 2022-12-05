from django.contrib import admin
from . import models
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','slug')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','descriptionCategory','slug')

admin.site.register(models.LessonModels,LessonAdmin)
admin.site.register(models.Category,CategoryAdmin)