# Generated by Django 2.1.5 on 2019-02-25 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestName', models.CharField(max_length=255)),
                ('MaxMarks', models.IntegerField()),
                ('TimeDuration', models.IntegerField()),
                ('PosMarks', models.IntegerField()),
                ('NegMarks', models.IntegerField()),
                ('InputTextFile', models.FileField(upload_to='Tests/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])])),
            ],
        ),
    ]
