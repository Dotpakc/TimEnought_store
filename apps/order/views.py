from django.db import transaction
from django.shortcuts import render , redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#messages
from django.contrib import messages
from django.views.generic import View

from config.settings import PAGE_NAMES

from .forms import AddCartForm, OrderCreateForm
from .models import Cart, Order, OrderProduct
from apps.catalog.models import Product

# Create your views here.

def get_cart_data(user_id):
    cart = Cart.objects.filter(user=user_id)
    total = 0
    for row in cart:
        total += row.product.price * row.quantity
    return {'cart': cart, 'total': total}



class AddToCartView(LoginRequiredMixin, View):
    def get(self, request):
        data = request.GET.copy()  # копіюємо дані з GET запиту
        data.update(user=request.user)  # додаємо дані про користувача
        request.GET = data  # перезаписуємо GET запит
        form = AddCartForm(request.GET)  # створюємо форму
        
        if form.is_valid():
            cd = form.cleaned_data
            row = Cart.objects.filter(product=cd['product'], user=cd['user']).first()
            if row:
                # Cart.objects.filter(id=row.id).update(quantity=cd['quantity'])
                row.quantity = cd['quantity']
                row.save()
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


class CartView(LoginRequiredMixin, View):
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


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        error = None
        user = request.user
        cart = get_cart_data(user.id)
               
        if not cart['cart']:
            error = 'Кошик порожній'
            messages.error(request, error, extra_tags='danger')
            return redirect(reverse('cart'))
        
        form = OrderCreateForm(data={
            'first_name': user.first_name if user.first_name else '',
            'last_name': user.last_name if user.last_name else '',
            'email': user.email if user.email else '',
            'phone': user.phone if user.phone else '',
            'address': user.address if user.address else '',
        })

        return render(request,
                        'order/order_create.html',
                        {'form': form,
                         'cart': cart,
                         'error': error,
                         'breadcrumbs': self.get_breadcrumbs()})
            
    def post(self, request):
        user = request.user
        cart = get_cart_data(user.id)
        
        data = request.POST.copy()
        data.update(user=user.id)
        data.update(total=cart['total'])
        data.update(paid=False)
        request.POST = data
        form = OrderCreateForm(request.POST)
        print(request.POST)
        if form.is_valid():
            order = form.save()
            # Очистити корзину і додати товари до замовлення в одній транзакції
            with transaction.atomic():
                for row in cart['cart']:
                    quantity = row.quantity if row.quantity < row.product.quantity else row.product.quantity
                    OrderProduct.objects.create(
                        order=order,
                        product=row.product,
                        price=row.product.price,
                        quantity=quantity
                    )
                    Product.objects.filter(id=row.product.id).update(quantity=row.product.quantity - quantity)
                Cart.objects.filter(user=user.id).delete()
            return render(request,
                            'order/order_created.html',
                            {'order': order,
                             'breadcrumbs': self.get_breadcrumbs()})
        else:
            messages.error(request, 'Помилка оформлення замовлення', extra_tags='danger')
              
        return render(request,
                        'order/order_create.html',
                        {'form': form,
                         'cart': cart,
                         'breadcrumbs': self.get_breadcrumbs()})
    
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog'],
                          reverse('cart'): 'Кошик'}
        breadcrumbs['current'] = 'Оформлення замовлення'
        return breadcrumbs

class DeleteFromCartView(LoginRequiredMixin, View):
    def get(self, request, pk):
        get_object_or_404(Cart, user=request.user.id, product=pk).delete()
        # Cart.objects.filter(user=request.user.id, product=pk).delete()
        return redirect(reverse('cart'))
