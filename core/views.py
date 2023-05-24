from django.shortcuts import render

# Create your views here.
def frontpage(request):
    articles = [
        {'id': 1, 'title': 'First article', 'content': 'This is the first article'},
        {'id': 2, 'title': 'Second article', 'content': 'This is the second article'},
        {'id': 3, 'title': 'Third article', 'content': 'This is the third article'},
        {'id': 4, 'title': 'Fourth article', 'content': 'This is the fourth article'},
        {'id': 5, 'title': 'Fifth article', 'content': 'This is the fifth article'},
        {'id': 6, 'title': 'Sixth article', 'content': 'This is the sixth article'},
    ]
    return render(request, 'core/frontpage.html', {'articles': articles})

