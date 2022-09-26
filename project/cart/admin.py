from django.contrib import admin
from cart.models import Category,Product,Profile,Orderitem,Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Orderitem)
admin.site.register(Order)
