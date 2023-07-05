from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddCartForm
from .models import Cart

from django.http import HttpResponse

# Create your views here.

def get_cart_data(user_id):
    cart = Cart.objects.filter(user=user_id)
    total = 0
    for row in cart:
        total += row.product.price * row.quentity
    return {'cart': cart, 'total': total}



def add_to_cart(request):
    data = request.GET.copy() # копіюємо дані з GET запиту
    data.update({'user': request.user.id}) # додаємо дані про користувача
    request.GET = data # перезаписуємо GET запит
    form = AddCartForm(request.GET) # створюємо форму
    print(form)
    print(form.is_valid()) # перевіряємо чи дані валідні 
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        row = Cart.objects.filter(product=cd['product'], user=cd['user'])
        if row:
            Cart.objects.filter(id = row.id).update(quentity=row.quentity+ cd['quentity'])
        else:
            form.save()
        return render(request,
                    'order/added.html',
                    {'product': cd['product'],
                    'cart': get_cart_data(cd['user'])}
                    )       
    else:
        return HttpResponse('ДОРОБИ МЕНЕ!!!')
                    