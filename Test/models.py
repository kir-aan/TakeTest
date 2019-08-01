from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def content_file_name(instance, filename):
    return "Tests/{subfolder}/{folder}/{file}".format(subfolder=instance.Uploader_info, folder=instance.TestName, file=filename)

def validate_file_extension(value):
    if value.file.content_type != 'text/plain':
        raise ValidationError('The uploaded file must be a text file')

class TestInfo(models.Model):
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='testinfos', on_delete=models.CASCADE, null=True)
    TestName = models.CharField(max_length=255)
    MaxMarks = models.IntegerField()
    TimeDuration = models.IntegerField()
    PosMarks = models.IntegerField()
    NegMarks = models.IntegerField()
    InputTextFile = models.FileField(upload_to=content_file_name, blank=False, validators=[validate_file_extension])
    date =  models.DateTimeField(auto_now=True)
    def __str__(self):
        template = '{0.TestName} {0.Uploader_info}'
        return template.format(self)
