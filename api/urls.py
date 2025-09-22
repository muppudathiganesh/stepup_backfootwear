from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import ProductsByCategoryAPIView
from .views import ContactMessageView



urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
     path('api/contact/', ContactMessageView.as_view(), name='contact-message'),
   
]
