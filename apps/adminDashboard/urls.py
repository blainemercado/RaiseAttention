from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^admin$', views.admin, name = 'admin'),
	url(r'^login$', views.login, name = 'adminLogin'),
	url(r'^logout$', views.logout, name = 'adminLogout'),
	url(r'^adminDash$', views.adminDash, name = 'adminDash'),
	url(r'^npo/switchActive/(?P<id>\d+)$', views.switchActive, name = 'adminSwitchActive'),
	url(r'^npo/resetVote/(?P<id>\d+)$', views.resetVote, name = 'adminResetVote'),
	url(r'^visitors/resetCount/(?P<id>\d+)$', views.resetVisitorCount, name = 'adminResetVote')
]
