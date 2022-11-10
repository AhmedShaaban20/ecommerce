from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(User_Address)
admin.site.register(User_Payment)
admin.site.register(Shopping_Session)
admin.site.register(Product_Category)
admin.site.register(Product_Inventory)
admin.site.register(Discount)
admin.site.register(Product)


# admin.site.register(Article)
# admin.site.register(Reporter)

