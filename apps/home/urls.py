from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'home_index'),
	url(r'^support$', views.support, name = 'home_support')
]