from django.contrib import admin
from . import models
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','slug','create_date','update_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

admin.site.register(models.LessonModels,LessonAdmin)
admin.site.register(models.Category,CategoryAdmin)