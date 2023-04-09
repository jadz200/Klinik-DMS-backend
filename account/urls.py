from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.apiOverview, name="api-overview") ,
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    ]
