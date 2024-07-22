from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=150, default = 'Other')
    about = models.CharField(max_length=200, null=True, blank = True)
    # Add all the products under these categories
    
    def __str__(self):
        return str(self.title)


class ProductModel(models.Model):
    productname = models.CharField(max_length=50, null=True)
    price = models.PositiveBigIntegerField()
    description = models.CharField(max_length=200)
    category = models.ManyToManyField(CategoryModel, related_name = 'category')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # products = models.ManyToManyField(SellerModel, related_name = 'products')
    
    
    def __str__(self):
        return str(self.productname)
    


    

class SellerModel(models.Model):
    sellername = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    products = models.ManyToManyField(ProductModel, related_name = 'products')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.sellername)
    

class ReviewModel(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=100)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.product) + "   reviewed by -> " + str(self.review_user)
    
