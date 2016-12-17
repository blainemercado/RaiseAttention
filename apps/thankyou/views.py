from django.shortcuts import render, redirect
from .models import *
from django.core.urlresolvers import reverse

# Create your views here.
def thankyou(request):
	return render(request, 'thankyou/thankyou.html')

def addSupporter(request):
	if request.method != 'POST':
		return redirect(reverse('thankyou:thankyou'))
	supporter = request.POST
	createdSupporter = Supporter.supporterManager.create(supporter)
	print('*-*-*-*-*-*-*-')
	print(createdSupporter)
	return redirect(reverse('thankyou:thankyou'))
