from django import forms
from django.forms import ModelForm
from budget.models import Person

class NameForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'income']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    