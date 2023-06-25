from django.shortcuts import render

from apps.blog.models import Article

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html', {'title': 'Главна сторінка'})

def about(request):
    return render(request, 'core/about.html', {'title': 'O нас'})