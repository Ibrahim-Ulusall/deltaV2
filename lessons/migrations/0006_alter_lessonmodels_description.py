# Generated by Django 4.1.3 on 2022-12-06 12:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_alter_lessonmodels_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonmodels',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
