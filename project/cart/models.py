from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categorylist')

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default="defaultpic.png",upload_to='products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    seller = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('productdetail',kwargs={'pk':self.pk})




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="defaultprofile.png",upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)

        if img.height>200 or img.width>200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()

class Orderitem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def totalprice(self):
        return self.product.price*self.quantity

    def __str__(self):
        return '{0}-{1}'.format(self.customer,self.product.title)

    def get_absolute_url(self):
        return reverse('orderlist')


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default = False)
    items = models.ManyToManyField(Orderitem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        total=0
        for order_item in self.items.all():
            total+=order_item.totalprice()
        return total

    def get_absolute_url(self):
        return reverse('orderlist')
