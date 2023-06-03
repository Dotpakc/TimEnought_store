from django.shortcuts import render, get_object_or_404, redirect


from .forms import CommentForm
from .models import Article
# Create your views here.
def details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
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
    article = Article.objects.order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/list.html', {'articles': articles,'title': "Blog - головна сторінка"})

def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__name=tag)
    return render(request, 'blog/articles_tag_list.html', {'articles': articles, 'title': tag})


def tag_list(request, tag):
   pass