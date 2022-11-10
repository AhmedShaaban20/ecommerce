from email.policy import default
from django.db import models
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  
    email = models.EmailField(max_length=200, unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    telephone = models.IntegerField(blank=True, null=True) 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email

class User_Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    address_line1= models.CharField(max_length=200, blank=True, null=True)
    address_line2= models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    payment_type= models.CharField(max_length=100, blank=True, null=True)

class User_Payment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    payment_type= models.CharField(max_length=100, blank=True, null=True)
    provider= models.CharField(max_length=100, blank=True, null=True)
    account_no = models.IntegerField(blank=True, null=True)
    expiry = models.DateField()

class Shopping_Session(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    total= models.DecimalField(decimal_places=6,max_digits=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Product_Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class Product_Inventory(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class Discount(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount_percent = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    category_id = models.ForeignKey(Product_Category,related_name="Product_category_id", on_delete=models.PROTECT)
    inventory_id = models.ForeignKey(Product_Inventory,related_name="Product_inventory_id", on_delete=models.PROTECT)
    discount_id = models.ForeignKey(Discount,related_name="Discount_discount_id",blank=True,null=True, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class Cart_Item(models.Model):
    session_id = models.ForeignKey(Shopping_Session, related_name="Cart_Item_session_id",on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product,related_name="Product_product_id",on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Payment_Details(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Order_Details(models.Model):
    user_id = models.ForeignKey(User, related_name="Order_Details_user_id",on_delete=models.DO_NOTHING)
    total = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    payment_id = models.ForeignKey(Payment_Details,related_name="Order_Details_payment_id",on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Order_Items(models.Model):
    order_id = models.ForeignKey(Order_Details, related_name="Order_Items_order_id",on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product,related_name="Order_Items_product_id",on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline