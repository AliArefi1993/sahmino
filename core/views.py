from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DoneByEnum, Item, ItemStatusEnum, ItemTypeEnum
from .serilizers import ItemSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """Retrieve an item by id and allow updating (PUT/PATCH)."""

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


# Endpoint to return total GVT earned per person for tasks with status='Done'
class DoneByGvtTotalsView(APIView):
    def get(self, request):
        # Sum gvt_earned grouped by done_by for items marked Done
        qs = (
            Item.objects.filter(status=ItemStatusEnum.DONE.value)
            .values("done_by")
            .annotate(total_gvt=Sum("gvt_earned"))
        )
        # Map results for quick lookup
        totals_map = {entry["done_by"]: entry["total_gvt"] for entry in qs}

        # Ensure every configured person is returned (0 if none)
        results = []
        for name, _ in DoneByEnum.choices():
            total = totals_map.get(name) or 0
            # Serialize Decimal to string for JSON stability
            results.append({"done_by": name, "total_gvt": str(total)})

        return Response({"totals": results})
