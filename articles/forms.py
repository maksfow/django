from django import forms
from .models import Article
from django.forms import ModelForm,TextInput,Textarea,FileInput,Select
class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)
from django import forms
from .models import Article

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Textarea(attrs={'class': 'form-control'})
        }
