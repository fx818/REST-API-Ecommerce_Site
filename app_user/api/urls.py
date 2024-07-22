from django.urls import path, include
from . import views
from app_user import models

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    
    # for registration
    path('register/', views.registration_view, name='register'),   
   
    # Using JWT Auth for login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
    