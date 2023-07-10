from django.contrib import admin

# Register your models here.
from .models import Order

# admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'first_name', 'last_name', 'email', 'phone', 'address', 'comments', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid']    
    search_fields = ['id', 'user', 'total', 'first_name', 'last_name', 'email', 'phone', 'address', 'comments', 'created', 'updated', 'paid']
    # readonly_fields = ['id', 'user', 'total', 'first_name', 'last_name', 'email', 'phone', 'address', 'comments', 'created', 'updated']
