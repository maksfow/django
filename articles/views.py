from django.shortcuts import render
from . import forms

def home(request):
    search_bar = forms.SearchForm()
    upload_form = forms.SearchForm()
    context = {"search_form": search_bar, "upload_form": upload_form}
    return render(request,'home.html',context)

def info(request):
    if request.method == 'POST':
        pass

def review(request):
    if request.method == 'POST':
        pass
def look(request):
    return render(request,'look.html')
def about(request):
    return render(request,'about.html')
