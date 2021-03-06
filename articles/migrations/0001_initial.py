# Generated by Django 2.1.7 on 2019-03-25 18:16

import articles.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='draft', max_length=20)),
                ('publish', models.DateTimeField(default=articles.models.default_start_time)),
                ('title', models.CharField(max_length=280)),
                ('slug', models.SlugField(blank=True, default='', max_length=280, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=160, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('post_thumb', models.ImageField(blank=True, null=True, upload_to='post_thumbs/')),
                ('post_image_alt', models.CharField(blank=True, max_length=280, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete='SET_DEFAULT', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
                'ordering': ('-publish',),
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=165, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'tag',
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='articles.Tag'),
        ),
    ]
