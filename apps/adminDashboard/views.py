from django.shortcuts import render, redirect
from ..home.models import *
from ..thankyou.models import *
from django.core.urlresolvers import reverse

# Create your views here.
def admin(request):
	return render(request, 'adminDashboard/adminLoginPage.html')

def login(request):
	if request.method != 'POST':
		return redirect('/adminDashboard/admin')
	password = request.POST['password']
	if password == "0Dec0Hat":
		request.session['password'] = password
		return redirect('/adminDashboard/adminDash')
	else:
		return redirect('/adminDashboard/admin')

def logout(request):
	del request.session['password']
	return redirect('/adminDashboard/admin')

def adminDash(request):
	if 'password' not in request.session:
		return redirect('/adminDashboard/admin')
	else:
		npoArray = Npo.npoManager.voteCount()
		supportersArray = Supporter.supporterManager.getSupporters()
		visitorsArray = SiteVisitors.visitorsManager.getVisitors()
		for npo in npoArray:
			print("total votes for ", npo.name, npo.votes)
		for supporter in supportersArray:
			print(supporter.ageRange)
		context = {
			"npos": npoArray,
			"supporters": supportersArray,
			"visitors": visitorsArray
		}
		return render(request, 'adminDashboard/admin.html', context)

def switchActive(request, id):
	Npo.npoManager.active(id)
	return redirect('/adminDashboard/adminDash')