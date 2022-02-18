# Generated by Django 3.2.9 on 2022-02-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_page_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]