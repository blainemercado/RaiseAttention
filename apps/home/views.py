from django.shortcuts import render, redirect
from .models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	totalVisitors = SiteVisitors.visitorsManager.addTotalVisitors('totalVisitors')
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
	try:
		created = Npo.npoManager.create(npoName)
	except:
		context = {
			"error": ["Error recording your vote. Please try voting again"]
		}
		return render(request, 'home/index.html', context)
	if created == True:
		return redirect(reverse('thankyou:thankyou'))
	else:
		count = Npo.npoManager.addVote(npoName)
		return redirect(reverse('thankyou:thankyou'))