from django.contrib import admin
from shop.models import Product, Orders, allabout, task


# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(allabout)
admin.site.register(task)