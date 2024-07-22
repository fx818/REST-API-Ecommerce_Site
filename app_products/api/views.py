from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer, SellerSerializer, ReviewSerializer
from app_products import models
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .pagination import CustomPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class sellerView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = models.SellerModel.objects.all()
    serializer_class = SellerSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['sellername',]
    filterset_fields = ['active']
    ordering_fields = ['created', 'updated']
    
class sellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = models.SellerModel.objects.all()
    serializer_class = SellerSerializer

class categoryView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = models.CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','about']



class productView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = models.ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['productname', 'price']
    filterset_fields = ['price', 'active']
    ordering_fields = ['price', 'created', 'updated']

    
class productDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = models.ProductModel.objects.all()
    serializer_class = ProductSerializer
    
    
class reviewView(generics.ListAPIView):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['rating', 'active']
    ordering_fields = ['rating', 'created', 'updated']
    # queryset = models.ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.ReviewModel.objects.filter(product = pk)
    
    

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return models.ReviewModel.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        data = models.ProductModel.objects.get(pk= pk)
        review_user = self.request.user
        review_queryset = models.ReviewModel.objects.filter(product = data, review_user = review_user)
     
        if review_queryset.exists():
            raise ValidationError("You have already reviewed")
        data.save()
        serializer.save(product = data, review_user = review_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    queryset = models.ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    
class UserreviewView(generics.ListAPIView):

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['rating', 'active']
    ordering_fields = ['rating','created', 'updated']
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.ReviewModel.objects.filter(review_user = pk)
    

