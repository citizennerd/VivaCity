from django.db import models

class DMS(models.Model):
	name = models.CharField(max_length=250)
	base_address = models.URLField()
	type = models.CharField(max_length=250)
	API_Key = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name
	
class DMSType(models.Model):
	name = models.CharField(max_length=250)
	module = models.CharField(max_length=250)

	def __self__(self):
		return self.name
