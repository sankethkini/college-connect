# Generated by Django 3.1.3 on 2020-12-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0014_auto_20201129_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='research',
            name='duration',
            field=models.IntegerField(default=30),
        ),
    ]
