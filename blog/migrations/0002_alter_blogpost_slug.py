# Generated by Django 5.0.4 on 2024-05-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL'),
        ),
    ]
