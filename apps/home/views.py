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
	npoName = request.POST['npo']
	created = Npo.npoManager.create(npoName)
	if created == True:
		return redirect(reverse('thankyou:thankyou'))
	else:
		count = Npo.npoManager.addVote(npoName)
		return redirect(reverse('thankyou:thankyou'))