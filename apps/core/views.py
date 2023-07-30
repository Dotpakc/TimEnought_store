from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse

from .mixins import DetailViewBreadcrumbMixin
from .models import Page


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