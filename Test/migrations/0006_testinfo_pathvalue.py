# Generated by Django 2.1.7 on 2019-03-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_testinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinfo',
            name='pathValue',
            field=models.CharField(default='<django.db.models.fields.files.FileField>', editable=False, max_length=500),
        ),
    ]