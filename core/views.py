from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DoneByEnum, Item, ItemTypeEnum
from .serilizers import ItemSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Endpoint to get allowed item types
class ItemTypeChoicesView(APIView):
    def get(self, request):
        types = [choice[0] for choice in ItemTypeEnum.choices()]
        return Response({"types": types})


# Endpoint to get allowed done_by values
class DoneByChoicesView(APIView):
    def get(self, request):
        done_by = [choice[0] for choice in DoneByEnum.choices()]
        return Response({"done_by": done_by})
