from django.urls import path

from .views import (
    DoneByChoicesView,
    ItemDeleteView,
    ItemListCreateView,
    ItemRetrieveUpdateView,
    ItemTypeChoicesView,
)

urlpatterns = [
    path("items/", ItemListCreateView.as_view(), name="item-list-create"),
    path(
        "items/<int:pk>/", ItemRetrieveUpdateView.as_view(), name="item-retrieve-update"
    ),
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
    path("item-types/", ItemTypeChoicesView.as_view(), name="item-type-choices"),
    path("done-by/", DoneByChoicesView.as_view(), name="done-by-choices"),
]
