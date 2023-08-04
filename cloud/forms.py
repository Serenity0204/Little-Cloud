from django import forms
from .models import File


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ("title", "description", "file_type", "img", "pdf", "doc", "txt")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "file_type": forms.Select(attrs={"class": "form-control"}),
            "img": forms.FileInput(
                attrs={"class": "form-control-file", "accept": "image/*"}
            ),
            "pdf": forms.FileInput(
                attrs={"class": "form-control-file", "accept": ".pdf"}
            ),
            "doc": forms.FileInput(
                attrs={"class": "form-control-file", "accept": ".doc,.docx"}
            ),
            "txt": forms.FileInput(
                attrs={"class": "form-control-file", "accept": ".txt"}
            ),
        }
