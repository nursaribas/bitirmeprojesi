from django import forms
from file.models import Document, File
from django.forms import ClearableFileInput
#from uploads.core.models import Document


class FileForm(forms.ModelForm):
   class Meta:
        model= File
        fields= ["name","description","filepath","publishing_date"] #file dosyasındaki ayrıntılar
        widgets = {
            'media': ClearableFileInput(attrs={'multiple': True})
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        #fields = ('name', 'filepath')
        fields= ["name", "description","filepath","publishing_date"]


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


