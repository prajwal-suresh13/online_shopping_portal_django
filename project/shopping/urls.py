"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from cart.views import (CategoryLV,CategoryDV,ProductDV,CategoryCreate,ProductLV,register,profile,CategoryUpdate,CategoryDelete,ProductCreate,
                        ProductDelete,ProductUpdate,add_to_cart,remove_from_cart,removesingle,mycart,delivery,payment,updateprofile,
                        UserList,OrderLV,OrderDV,OrderUpdate,
                        OrderDelete,OrderitemDV,OrderitemUpdate,
                        OrderitemDelete,UserDetail,UserUpdate,UserDelete)
from cart import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name='register'),
    path('',ProductLV.as_view(),name='productlist'),
    path('login/',auth_views.LoginView.as_view(template_name='cart/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='cart/logout.html'),name='logout'),
    path('profile/',profile,name='profile'),
    path('delivery/',delivery,name='delivery'),
    path('payment/',payment,name='payment'),
    path('users/',UserList.as_view(),name='userlist'),
    path('users/<pk>/',UserDetail.as_view(),name='userdetail'),
    path('users/<pk>/update/',UserUpdate.as_view(),name='userupdate'),
    path('users/<pk>/delete/',UserDelete,name='userdelete'),








    path('orders/',OrderLV.as_view(),name='orderlist'),
    path('orders/<pk>/',OrderDV.as_view(),name='orderdetail'),
    path('orders/<pk>/update/',OrderUpdate.as_view(),name='orderupdate'),
    path('orders/<pk>/delete/',OrderDelete.as_view(),name='orderdelete'),

    path('orderitem/<pk>/',OrderitemDV.as_view(),name='orderitemdetail'),
    path('orderitem/<pk>/update/',OrderitemUpdate.as_view(),name='orderitemupdate'),
    path('orderitem/<pk>/delete/',OrderitemDelete.as_view(),name='orderitemdelete'),










    path('categories/',CategoryLV.as_view(),name='categorylist'),
    path('categories/add/',CategoryCreate.as_view(),name='categorycreate'),
    path('categories/<pk>/',CategoryDV.as_view(),name='categorydetail'),
    path('categories/<pk>/update/',CategoryUpdate.as_view(),name='categoryupdate'),
    path('categories/<pk>/delete/',CategoryDelete.as_view(),name='categorydelete'),
    path('product/addp/',ProductCreate.as_view(),name='productcreate'),
    path('product/<pk>/',ProductDV.as_view(),name='productdetail'),
    path('product/<pk>/updatep/',ProductUpdate.as_view(),name='productupdate'),
    path('product/<pk>/deletep/',ProductDelete.as_view(),name='productdelete'),
    path('mycart/',mycart,name='mycart'),
    path('updateprofile/',updateprofile,name='updateprofile'),

    path('<pk>/addtocart/',add_to_cart,name='addtocart'),
    path('<pk>/removefromcart/',remove_from_cart,name='removefromcart'),
    path('<pk>/removesingle/',removesingle,name='removesingle'),









]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
fjdfjdfjksdfjaskjflka;jfsflkdjfd