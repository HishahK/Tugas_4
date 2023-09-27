from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('item/<int:item_id>/<str:action>/', views.adjust_amount, name='adjust_amount'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
]
