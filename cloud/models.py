from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


# Create your models here.
class File(models.Model):
    FILE_TYPES = (
        ("img", "Image"),
        ("pdf", "PDF"),
        ("doc", "Document"),
        ("txt", "Text"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=35)
    description = models.TextField()
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    pdf = models.FileField(upload_to="pdfs/", null=True, blank=True)
    doc = models.FileField(upload_to="docs/", null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)

    file_type = models.CharField(max_length=4, choices=FILE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # Set the ordering to display instances from newest to oldest based on created_at.
        ordering = ["-created_at"]


@receiver(pre_delete, sender=File)
def delete_file_on_delete(sender, instance, **kwargs):
    # Delete associated files when the File instance is deleted
    if instance.img:
        # Delete the image file
        os.remove(instance.img.path)

    if instance.pdf:
        # Delete the PDF file
        os.remove(instance.pdf.path)

    if instance.doc:
        # Delete the Document file
        os.remove(instance.doc.path)
