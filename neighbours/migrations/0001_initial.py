# Generated by Django 2.2.4 on 2019-09-16 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(default='e.g Aries, Sagittarius, Leo', max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('occupants_count', models.IntegerField(blank=True, default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='images/')),
                ('contact', tinymce.models.HTMLField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post_hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbours.Neighborhood')),
                ('poster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbours.Neighborhood')),
                ('user_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('biz_hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biz', to='neighbours.Neighborhood')),
                ('biz_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
