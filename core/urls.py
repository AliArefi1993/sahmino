from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.get_items, name='get_items'),
    path('items/create/', views.create_item, name='create_item'),
]
