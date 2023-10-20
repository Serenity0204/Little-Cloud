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


class ShareFileForm(forms.Form):
    recipient_username = forms.CharField(
        label="Recipient's Username",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    selected_file = forms.ModelChoiceField(
        queryset=File.objects.none(),
        label="Select File",
        empty_label="Select a file",
        required=True,
        widget=forms.Select(attrs={"class": "form-select custom-select"}),
    )

    def __init__(self, user, *args, **kwargs):
        super(ShareFileForm, self).__init__(*args, **kwargs)

        self.fields["selected_file"].queryset = File.objects.filter(user=user)
