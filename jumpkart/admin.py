from django.contrib import admin

from .models  import  Product,Cart,MySiteUser,Reviews

# Register your models here.



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(MySiteUser)
admin.site.register(Reviews)
