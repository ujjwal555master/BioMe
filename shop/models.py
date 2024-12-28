from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    details = models.CharField(max_length=5000)
    feature = models.CharField(max_length=5000, default="")

    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class allabout(models.Model):
    user_id = models.CharField(max_length=23)
    coin = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user_id

class task(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='shop/images', default="")
    desc = models.CharField(max_length=3000)


