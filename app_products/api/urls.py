from django.urls import path
from .views import (categoryView, productView, sellerView,
                    reviewView, productDetailView, UserreviewView,
                    ReviewCreate, sellerDetailView, ReviewDetail)

urlpatterns = [
    
    path('category/', categoryView.as_view(), name = 'category'),
    path('allproducts/', productView.as_view(), name = 'all-product'),
    path('allproducts/<int:pk>/', productDetailView.as_view(), name = 'product-detail'),
    path('seller/', sellerView.as_view(), name = 'seller-list'),
    path('seller/<int:pk>', sellerDetailView.as_view(), name = 'seller-detail'),
    path('<int:pk>/review/', reviewView.as_view(), name = 'review-by-prod-id'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name = 'review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name = 'review-detail'),
    path('userreview/<int:pk>/', UserreviewView.as_view(), name = 'review-by-user'),

]