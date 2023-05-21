from django.shortcuts import render
from apps.blog.models import BlogCategory, Article

def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, "blog/category/list.html", {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(сategory=category_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, "blog/article/list.html", {'articles': articles, 'category': category})