from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class LessonModels(models.Model):
    
    title = models.CharField(max_length=50)
    description = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    update_date = models.DateTimeField(auto_now=True,verbose_name='Son Güncelleme Tarihi')
    slug = models.SlugField(db_index=True,unique=True,editable=False)
    
        
    def __str__(self) -> str:
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptionCategory = RichTextField()
    slug = models.SlugField(db_index=True,editable=False,unique=True)
    
    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)
        super().save(*args,**kwargs)