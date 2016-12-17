from django.shortcuts import render, redirect
from ..home.models import *
from ..thankyou.models import *
from django.core.urlresolvers import reverse

# Create your views here.
def admin(request):
	npoArray = Npo.npoManager.voteCount()
	supportersArray = Supporter.supporterManager.getSupporters()
	for npo in npoArray:
		print("total votes for ", npo.name, npo.votes)
	for supporter in supportersArray:
		print(supporter.ageRange)
	context = {
		"npos": npoArray,
		"supporters": supportersArray
	}
	return render(request, 'adminDashboard/admin.html', context)