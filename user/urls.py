from django.urls import path
from . import views

urlpatterns = [
    path('', views.room, name='user-room'),
    path('billing/', views.billing, name='user-billing'),
]