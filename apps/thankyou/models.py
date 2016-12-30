from __future__ import unicode_literals

from django.db import models

class SupporterManager(models.Manager):
	def create(self, supporter):
		print('*^*^*^*^*^*^^*^*^*^*^*^*^*^*^*^')
		returnSupporter = False
		for key in supporter:
			if key == 'returnSupporter':
				returnSupporter = True
		person = Supporter.objects.create(returnSupporter=returnSupporter, ageRange=supporter['ageRange'], gender=supporter['gender'], relationship=supporter['relationship'], state=supporter['state'], country=supporter['country'])
		print(person.returnSupporter)
		return True
	def getSupporters(self):
		supportersArray = Supporter.objects.all()
		return supportersArray

# Create your models here.
class Supporter(models.Model):
	returnSupporter = models.BooleanField()
	ageRange = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	relationship = models.CharField(max_length=25)
	state = models.CharField(max_length=20)
	country = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	supporterManager = SupporterManager()
	objects = models.Manager()