from django.db import models
from enum import Enum


class ItemStatusEnum(Enum):
	DONE = "Done"
	TODO = "To Do"
	IN_PROGRESS = "In Progress"

	@classmethod
	def choices(cls):
		return [(tag.value, tag.value) for tag in cls]


class DoneByEnum(Enum):
	ALI = "Ali"
	JAVAD = "Javad"
	AMIRREZA = "Amirreza"
	FOAD = "Foad"

	@classmethod
	def choices(cls):
		return [(tag.value, tag.value) for tag in cls]

class ItemTypeEnum(Enum):
	BRANDING = "Branding"
	FINANCE = "Finance"
	FUNDRAISING = "Fundraising"
	ADMIN_MEETINGS = "Admin/Meetings"
	PRODUCTION = "Production"
	SALE = "Sale"

	@classmethod
	def choices(cls):
		return [(tag.value, tag.value) for tag in cls]


class Item(models.Model):
	date = models.DateField()
	done_by = models.CharField(max_length=100, choices=DoneByEnum.choices(), blank=True)
	task = models.CharField(max_length=255)
	type = models.CharField(max_length=100, choices=ItemTypeEnum.choices())
	status = models.CharField(max_length=20, choices=ItemStatusEnum.choices(), default=ItemStatusEnum.TODO.value)
	quantity = models.IntegerField()
	base_gvt = models.DecimalField(max_digits=10, decimal_places=2)
	gvt_earned = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.date} - {self.task} by {self.done_by}"
