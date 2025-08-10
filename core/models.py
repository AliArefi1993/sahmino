
from django.db import models

class Item(models.Model):
	date = models.DateField()
	done_by = models.CharField(max_length=100)
	task = models.CharField(max_length=255)
	type = models.CharField(max_length=100)
	quantity = models.IntegerField()
	base_gvt = models.DecimalField(max_digits=10, decimal_places=2)
	gvt_earned = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.date} - {self.task} by {self.done_by}"

# Create your models here.
