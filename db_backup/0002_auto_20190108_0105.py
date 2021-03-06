# Generated by Django 2.1.5 on 2019-01-07 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='password',
        ),
        migrations.RemoveField(
            model_name='project',
            name='feature',
        ),
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='training',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='training',
            name='start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='work',
            name='start',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='project_feature',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Project'),
        ),
    ]
