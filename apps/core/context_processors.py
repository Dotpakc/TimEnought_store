
from apps.core.models import Page

def page_navigator(request):
    
    pages = Page.objects.filter(is_active=True)
    
    return {
        'page_navigator': pages
    }