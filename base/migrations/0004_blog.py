# Generated by Django 4.1.7 on 2023-04-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_item_onoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.CharField(max_length=255)),
                ('other_images', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('blogId', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]
