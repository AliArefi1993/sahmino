
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Item

@csrf_exempt
@require_http_methods(["POST"])
def create_item(request):
	try:
		data = json.loads(request.body)
		item = Item.objects.create(
			date=data["date"],
			done_by=data["done_by"],
			task=data["task"],
			type=data["type"],
			quantity=data["quantity"],
			base_gvt=data["base_gvt"],
			gvt_earned=data["gvt_earned"]
		)
		return JsonResponse({"id": item.id, "message": "Item created successfully."}, status=201)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)

@require_http_methods(["GET"])
def get_items(request):
	items = Item.objects.all().values()
	return JsonResponse(list(items), safe=False)
