from django.shortcuts import render, redirect
from .models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	totalVisitors = SiteVisitors.visitorsManager.addVisitors('totalVisitors')
	monthlyVisitors = SiteVisitors.visitorsManager.addVisitors('monthlyVisitors')
	return render(request, 'home/index.html')

def support(request):
	if request.method != 'POST':
		return redirect('/')
	try:
		npoName = request.POST['npo']
	except:
		context = {
			"error": ["Error recording your vote. Please try voting again"]
		}
		return render(request, 'home/index.html', context)
	created = Npo.npoManager.create(npoName)
	if created == True:
		return redirect(reverse('thankyou:thankyou'))
	else:
		count = Npo.npoManager.addVote(npoName)
		print("Count after voting: ", count)
		return redirect(reverse('thankyou:thankyou'))