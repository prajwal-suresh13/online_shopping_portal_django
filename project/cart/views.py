from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,Delivery,Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Category,Product,Profile,Orderitem,Order
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
class UserList(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = User
    fields = ['username','email']
    template_name="cart/user_list.html"

    def test_func(self):
        return self.request.user.is_superuser


class UserDetail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = User
    template_name="cart/user_detail.html"
    def test_func(self):
        return self.request.user.is_superuser

class UserUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = User
    fields=['username','email']
    template_name="cart/user_update.html"
    success_message="User is updated"
    def test_func(self):
        return self.request.user.is_superuser





@user_passes_test(lambda u: u.is_superuser)
def UserDelete(request,pk):
    user = User.objects.filter(id=pk)
    if user.exists():
        user.delete()
        messages.success(request,'User is deleted')
    else:
        messages.info(request,'User not found')
    return redirect(reverse('userlist'))

class ProductLV(LoginRequiredMixin,ListView):
    model = Product
    ordering = ['title']

class CategoryLV(LoginRequiredMixin,ListView):
    model = Category
    ordering = ['name']

class CategoryDV(LoginRequiredMixin,DetailView):
    model = Category


class ProductDV(DetailView):
    model = Product



class CategoryCreate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
    model = Category
    fields=['name']
    success_message="Category created"

    def test_func(self):
        return self.request.user.is_superuser

class CategoryUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Category
    fields = ['name']
    success_message="Category updated"


    def test_func(self):
        return self.request.user.is_superuser


class CategoryDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Category
    success_message="Category deleted"
    success_url = '/categories/'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDelete, self).delete(request, *args, **kwargs)



    def test_func(self):
        return self.request.user.is_superuser




class ProductCreate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
    model = Product
    fields = '__all__'
    success_message="Product created"

    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Product
    fields = '__all__'
    success_message="Product updated"


    def test_func(self):
        return self.request.user.is_superuser

class ProductDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Product
    success_url = '/categories/'
    success_message="Product deleted"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductDelete, self).delete(request, *args, **kwargs)



    def test_func(self):
        return self.request.user.is_superuser







class OrderLV(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Order
    ordering = ['customer']
    def test_func(self):
        return self.request.user.is_superuser

class OrderDV(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Order
    def test_func(self):
        return self.request.user.is_superuser

class OrderUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Order
    fields = '__all__'
    success_message="Order updated"


    def test_func(self):
        return self.request.user.is_superuser


class OrderDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Order
    success_url='/orders/'
    success_message="Order deleted"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrderDelete, self).delete(request, *args, **kwargs)



    def test_func(self):
        return self.request.user.is_superuser






class OrderitemDV(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DetailView):
    model = Orderitem
    def test_func(self):
        return self.request.user.is_superuser

class OrderitemUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Orderitem
    fields = '__all__'
    success_message="Orderitem updated"


    def test_func(self):
        return self.request.user.is_superuser

class OrderitemDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Orderitem
    success_url='/orders/'
    success_message="Orderitem deleted"


    def test_func(self):
        return self.request.user.is_superuser
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrderitemDelete, self).delete(request, *args, **kwargs)














def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request,f' Account created for {username}!')
             return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'cart/register.html',{'form':form})


@login_required
def profile(request):
    user_profile = User.objects.filter(username=request.user.username)[0]
    myorders =Order.objects.filter(is_ordered=True,customer=user_profile)


    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account is updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form,'myorders':myorders}

    return render(request,'cart/profile.html',context)



@login_required
def add_to_cart(request,pk):
    user_profile = get_object_or_404(User,username=request.user.username)
    product = Product.objects.filter(pk=pk).first()
    order_item,status = Orderitem.objects.get_or_create(customer=user_profile,product=product,is_ordered=False)
    user_order = Order.objects.filter(customer=user_profile,is_ordered=False)
    if user_order.exists():
        order = user_order[0]
        if order.items.filter(product = product).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request,"This product quantity was updated")
            return redirect(reverse('mycart'))
        else:
            order.items.add(order_item)
            messages.info(request,"Item added to cart")
            return redirect(reverse('mycart'))
    else:
        order=Order.objects.create(customer=user_profile)
        order.items.add(order_item)
        messages.info(request,"Item added to cart")
        return redirect(reverse('mycart'))

@login_required
def remove_from_cart(request,pk):
    product = Product.objects.filter(pk=pk).first()
    user_profile = get_object_or_404(User,username=request.user.username)
    order_item,status = Orderitem.objects.get_or_create(product=product,customer=user_profile,is_ordered=False)
    order_item.delete()
    messages.info(request,'Item has been removed')
    return redirect(reverse('mycart'))

@login_required
def removesingle(request,pk):
    user_profile = get_object_or_404(User,username=request.user.username)
    product = Product.objects.filter(pk=pk).first()
    user_order = Order.objects.filter(customer=user_profile,is_ordered=False)
    if user_order.exists():
        order = user_order[0]
        if order.items.filter(product=product).exists():
            order_item,status=Orderitem.objects.get_or_create(product=product,customer=user_profile,is_ordered=False)
            if order_item.quantity>1:
                order_item.quantity-=1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request,"Item quantity updated")
            return redirect('mycart')
        else:
            messages.info(request,"This item was not in your cart")
            return redirect('mycart')
    else:
        messages.info(request,"You do not have active order")
        return redirect('mycart')

def get_user_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(User, username=request.user.username)
    order = Order.objects.filter(customer=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required
def mycart(request, **kwargs):
    uorder = get_user_order(request)
    context = {
        'object': uorder
    }
    return render(request, 'cart/mycart.html', context)

@login_required
def updateprofile(request):
    user_profile = get_object_or_404(User, username=request.user.username)
    order = Order.objects.filter(customer=user_profile)
    order.update(is_ordered=True)
    orderitems=Orderitem.objects.filter(customer=user_profile,is_ordered=False)
    orderitems.update(is_ordered=True)
    profile=Profile.objects.get(user=request.user)


    messages.success(request,"Thank you! Your purchase was successful! ")
    return redirect(reverse('profile'))



def delivery(request):
    form=Delivery()
    return render(request,'cart/proceedtobuy.html',{'form':form})

def payment(request):
    form = Payment()
    return render(request,'cart/payment.html',{'form':form})
