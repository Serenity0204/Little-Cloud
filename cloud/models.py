from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
import random
import string


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
    description = models.TextField(max_length=350)
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    pdf = models.FileField(upload_to="pdfs/", null=True, blank=True)
    doc = models.FileField(upload_to="docs/", null=True, blank=True)
    txt = models.FileField(upload_to="txts/", null=True, blank=True)

    is_shared = models.BooleanField(default=False)
    file_type = models.CharField(max_length=4, choices=FILE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    # for validation
    def is_empty(self):
        # image
        if self.file_type == "img":
            return not self.img
        # pdf
        if self.file_type == "pdf":
            return not self.pdf
        # doc
        if self.file_type == "doc":
            return not self.doc
        # text
        if self.file_type == "txt":
            return not self.txt
        return True

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

    if instance.txt:
        # Delete the Text file
        os.remove(instance.txt.path)


## model for Short Url
class ShortUrl(models.Model):
    file = models.OneToOneField(
        File, on_delete=models.CASCADE, related_name="short_url"
    )
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    viewers = models.ManyToManyField(User, related_name="short_urls")

    def __str__(self):
        return self.short_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_unique_short_url()
        super(ShortUrl, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.viewers.clear()
        super(ShortUrl, self).delete(*args, **kwargs)

    def generate_unique_short_url(self, length=10):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = "".join(random.choice(characters) for _ in range(length))
            if not ShortUrl.objects.filter(short_url=short_url).exists():
                return short_url
