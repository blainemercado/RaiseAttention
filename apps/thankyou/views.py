from django.shortcuts import render, redirect
from .models import *
from ..home.models import *
from django.core.urlresolvers import reverse

# Create your views here.
def thankyou(request):
	npoArray = Npo.npoManager.voteCount()
	print(npoArray);
	context = {
		"npos": npoArray
	}
	return render(request, 'thankyou/thankyou.html', context)

def addSupporter(request):
	if request.method != 'POST':
		return redirect(reverse('thankyou:thankyou'))
	supporter = request.POST
	createdSupporter = Supporter.supporterManager.create(supporter)
	print('*-*-*-*-*-*-*-')
	print(createdSupporter)
	return redirect(reverse('thankyou:thankyou'))

