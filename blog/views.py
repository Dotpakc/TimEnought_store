from django.shortcuts import render, get_object_or_404, redirect


from .forms import CommentForm
from .models import Article
# Create your views here.
def details(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', id=id)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'article': article, 'form': form})

def random_article(request):
    article = Article.objects.order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/list.html', {'articles': articles})

def tag_list(request, tag):
   pass