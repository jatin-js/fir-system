from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login),
    # path('test', views.logintest),
    path('otp', views.otp),
    path('welcome', views.welcome),
]