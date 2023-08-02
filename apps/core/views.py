from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

from .mixins import DetailViewBreadcrumbMixin
from .models import Page
from apps.catalog.models import Product


# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html', {'title': 'Главна сторінка'})

def about(request):
    return render(request, 'core/about.html', {'title': 'O нас'})


class PageDetailView(DetailViewBreadcrumbMixin):
    model = Page
    template_name = 'core/page.html'
    
    
    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True) if not self.request.user.is_staff else Page.objects.all()
        return queryset

    def get_breadcrumbs(self):
        self.breadcrumbs = {
            reverse('index'): 'Головна',
            'current': self.object.name
        }
        return self.breadcrumbs
    
def autocomplete(request):
    if request.method == 'GET':
        query = request.GET.get('term', '')
        if query:
            results = Product.objects.filter(name__icontains=query)
        else:
            results = Product.objects.all()
        results_json = []
        results_json = [result.name for result in results]
        return JsonResponse(results_json, safe=False)