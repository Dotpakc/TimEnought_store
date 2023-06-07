from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .forms import CommentForm
from .models import Article
# Create your views here.

@login_required(login_url='/members/login/')
def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'article': article, 'form': form})

def random_article(request):
    article = Article.objects.filter(status='active').order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})


def articles_list(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/error_login.html', {'title': "Помилка доступу"})
    articles = Article.objects.filter(status='active')
    return render(request, 'blog/list.html', {'articles': articles,'title': "Blog - головна сторінка"})



@login_required(login_url='/members/login/')
def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__name=tag, status='active')
    return render(request, 'blog/articles_tag_list.html', {'articles': articles, 'title': tag})

@login_required(login_url='/members/login/')
def tag_list(request, tag):
   pass

@login_required(login_url='/members/login/')
def search(request):
   query = request.GET.get('query', '')
   
   articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(content_preview__icontains=query), status='active')
   
   return render(request, 'blog/search.html', {'articles': articles, 'title': "Пошук по сайту", 'query': query})
