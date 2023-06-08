from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    
    
    return render(request, 'members/login.html', {'title':'Login','form':form})

@login_required()
def profile_view(request):
    return render(request, 'members/profile.html', {'title':'Profile'})

@login_required()
def logout_view(request):
    logout(request)
    return redirect('index')