# Generated by Django 2.1.5 on 2019-01-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_auto_20190119_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
