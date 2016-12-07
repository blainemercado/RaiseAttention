from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^thankyou$', views.thankyou, name = 'thankyou'),
	# url(r'^supporter$', views.addSupporter, name = 'thankyou_supporter')
]