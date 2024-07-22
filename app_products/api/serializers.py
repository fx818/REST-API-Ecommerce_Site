from app_products import models
from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.response import Response

class CategorySerializer(serializers.ModelSerializer):
    allproducts = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.CategoryModel
        fields = '__all__'

    def get_allproducts(self, obj):
        data = models.ProductModel.objects.filter(category=obj)
        return ProductSerializer(data, many=True).data



class ProductSerializer(serializers.ModelSerializer):
    
    sellername = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.ProductModel
        fields = '__all__'
        
        

class SellerSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model = models.SellerModel
        # exclude = ('products',)
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only = True)
    review_user = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = models.ReviewModel
        fields = '__all__'
        
