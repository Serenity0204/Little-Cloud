from django.contrib import admin
from .models import File


# Register your models here.
# Custom admin class for File model
class FileAdmin(admin.ModelAdmin):
    list_display = ("title", "file_type", "user", "created_at")
    list_filter = ("file_type",)  # Add file_type to the filters on the admin panel


# Register the File model with the custom admin class
admin.site.register(File, FileAdmin)
