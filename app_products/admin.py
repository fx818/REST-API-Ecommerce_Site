from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.SellerModel)
admin.site.register(models.ProductModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.ReviewModel)
