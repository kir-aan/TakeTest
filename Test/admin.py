from django.contrib import admin
from .models import TestInfo

class TestInfoAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.Uploader_info = request.user.username
        obj.save()

admin.site.register(TestInfo, TestInfoAdmin)
