
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('date', 'done_by', 'task', 'type', 'quantity', 'base_gvt', 'gvt_earned')
