from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from config.settings import PAGE_NAMES

from .forms import AddCartForm
from .models import Cart

# Create your views here.

def get_cart_data(user_id):
    cart = Cart.objects.filter(user=user_id)
    total = 0
    for row in cart:
        total += row.product.price * row.quantity
    return {'cart': cart, 'total': total}



class AddToCartView(View):
    def get(self, request):
        data = request.GET.copy()  # копіюємо дані з GET запиту
        data.update(user=request.user)  # додаємо дані про користувача
        request.GET = data  # перезаписуємо GET запит
        form = AddCartForm(request.GET)  # створюємо форму
        print(form)
        print(form.is_valid())  # перевіряємо чи дані валідні

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            row = Cart.objects.filter(product=cd['product'], user=cd['user']).first()
            if row:
                Cart.objects.filter(id=row.id).update(quantity=cd['quantity'])
            else:
                form.save()
            return render(request,
                          'order/added.html',
                          {'product': cd['product'],
                           'cart': get_cart_data(cd['user']),
                           'breadcrumbs': self.get_breadcrumbs()})  # Додайте breadcrumbs до контексту

    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        breadcrumbs[reverse('cart')] = 'Кошик'  # Посилання на корзину
        breadcrumbs['current'] = 'Додано'  # Поточна сторінка
        return breadcrumbs


class CartView(View):
    def get(self, request):
        user_id = request.user.id
        return render(request,
                      'order/cart_list.html',
                      {'cart': get_cart_data(user_id),
                       'breadcrumbs': self.get_breadcrumbs()})  # Додайте breadcrumbs до контексту

    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        breadcrumbs['current'] = 'Кошик'  # Поточна сторінка
        return breadcrumbs

