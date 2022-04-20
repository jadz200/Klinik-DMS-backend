from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',RegistrationAPIView.as_view(),name="register_profile"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),

    ]
