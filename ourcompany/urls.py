from django.urls import path,include
from .import views

urlpatterns = [
	path('',views.home,name='home'),
	path('event/',views.event,name='event'),
	path('event_past',views.past,name='past'),
	path('event_latest/',views.latest,name='latest'),
	path('event_upcoming/',views.upcoming,name='upcoming'),
	path('event_workshops/',views.workshops,name='workshops'),
	path('event_meetups/',views.meetups,name='meetups'),
	path('signup/',views.signup,name='signup'),
	path('accounts/',include('django.contrib.auth.urls')),
	path('research/',views.research,name='research'),
	path('userprofile/',views.profile,name='profile'),
]