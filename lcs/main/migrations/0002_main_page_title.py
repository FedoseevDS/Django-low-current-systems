# Generated by Django 3.2.9 on 2022-02-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_page',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
