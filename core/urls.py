
from django.urls import path
from .views import ItemListCreateView, ItemDeleteView, ItemTypeChoicesView, DoneByChoicesView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('item-types/', ItemTypeChoicesView.as_view(), name='item-type-choices'),
    path('done-by/', DoneByChoicesView.as_view(), name='done-by-choices'),
]
