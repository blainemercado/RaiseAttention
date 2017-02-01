from __future__ import unicode_literals

from django.db import models

class NpoManager(models.Manager):
	def create(self, name):
		npoList = Npo.objects.all()
		for npo in npoList:
			if npo.name == name:
				return False
		Npo.objects.create(name=name, votes=1)
		return True
	def addVote(self, name):
		npoObject = Npo.objects.get(name=name)
		npoObject.votes += 1
		npoObject.save()
		count = npoObject.votes
		return count
	def voteCount(self):
		npoArray = Npo.objects.all()
		return npoArray
	def active(self, id):
		npoObject = Npo.objects.get(id=id)
		if npoObject.active:
			npoObject.active = False
		else:
			npoObject.active = True
		npoObject.save()
		return True

class VisitorsManager(models.Manager):
	def addTotalVisitors(self, name):
		try:
			visitorsObject = SiteVisitors.objects.get(name=name)
		except:
			visitorsObject = SiteVisitors.objects.create(name=name, visitorCount=1)
			return visitorsObject.visitorCount
		visitorsObject.visitorCount += 1
		visitorsObject.save()
		return visitorsObject.visitorCount
	def getVisitors(self):
		visitorsArray = SiteVisitors.objects.all()
		return visitorsArray

# Create your models here.
class Npo(models.Model):
	name = models.CharField(max_length=300)
	votes = models.PositiveIntegerField()
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	npoManager = NpoManager()
	objects = models.Manager()

class SiteVisitors(models.Model):
	name = models.CharField(max_length=20)
	visitorCount = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	visitorsManager = VisitorsManager()
	objects = models.Manager()




