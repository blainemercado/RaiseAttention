from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def thankyou(request):
	return render(request, 'thankyou/thankyou.html')