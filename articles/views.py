from django.shortcuts import render,redirect
from . import forms
from .models import Category,Article
from .forms import SearchForm,ArticlesForm

def home(request):
    #  форма для поиска товаров на сайте
    search_bar = forms.SearchForm()
    upload_form = forms.SearchForm()
    article_info = Article.objects.all()
    # Собираем все категории товаров
    category_info = Category.objects.all()
    # Отправить элементы на фронт
    context = {"search_form": search_bar, "upload_form": upload_form, 'article': article_info, 'category': category_info}
    return render(request, 'home.html', context)




def category(request, pk):
    category = Category.objects.get(id=pk)
    articles = Article.objects.filter(category_name=category)
    context = {'articles': articles}
    return render(request, 'category.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)



def search_article(request):
    if request.method == 'POST':
        info = request.POST.get('search_article')
        try:
            infot = Article.objects.get(title__icontains=info)
            return redirect(f'article/{infot.id}')
        except:
            return redirect('/not-found')






def createarticles(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticlesForm()
    return render(request, 'createarticles.html', {'form': form})





def about(request):
    return render(request,'about.html')
def not_found(request):
    return render(request,'not-found.html')
def del_from_article(request,pk):
    article_to_delete = Article.objects.get(id=pk)
    Article.objects.all(user_id=request.user.id,
                        title=article_to_delete).delete()
    return redirect('/article')