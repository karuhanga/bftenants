# Generated by Django 2.2.5 on 2019-09-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]