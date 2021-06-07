from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='medicap-home'),
    path('login/', views.login, name='medicap-login'),
]