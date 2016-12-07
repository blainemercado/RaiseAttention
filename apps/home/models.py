from __future__ import unicode_literals

from django.db import models

class NpoManager(models.Manager):
	def create(self, name):
		npoList = Npo.objects.all()
		for npo in npoList:
			print('!@!@!@!@!@!@!@!!@!@!@!')
			print(npo.name)
			if npo.name == name:
				return False
		Npo.objects.create(name=name, votes=1)
		return True
	def addVote(self, name):
		npoObject = Npo.objects.get(name=name)
		count = npoObject.votes
		print('in models', count)
		npoObject.votes += 1
		npoObject.save()
		count = npoObject.votes
		print('in models after addition', count)
		return count

# Create your models here.
class Npo(models.Model):
	name = models.CharField(max_length=300)
	votes = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	npoManager = NpoManager()
	objects = models.Manager()