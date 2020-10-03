from django.shortcuts import render,redirect
from .models import PastEvent,LatestEvent,UpcomingEvent,WorkshopEvent,MeetupsEvent
from django.core.paginator import Paginator,Page
from django.contrib.auth.models import User,auth
from django.contrib import messages



def research(request):
    return render(request,'main/research.html',{'title':'Dashboard'})
# main_page
def home(request):
	return render(request,'ourcompany/home.html',{'title':'Home'})


#event_page
def event(request):
    event = PastEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'ourcompany/events.html',{'title':'Event','event':event})


#past_page
def past(request):
    event = PastEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'event/past.html',{'title':'past','event':event})


#latest_page
def latest(request):
    event = LatestEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'event/latest.html',{'title':'latest','event':event})

#meetups_page
def meetups(request):
    event = MeetupsEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'event/meetups.html',{'title':'meetups','event':event})

#workshops_page
def workshops(request):
    event = WorkshopEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'event/workshops.html',{'title':'workshops','event':event})

#upcoming_page
def upcoming(request):
    event = UpcomingEvent.objects.order_by('-id')
    paginator = Paginator(event,2)
    page = request.GET.get('page')
    event = paginator.get_page(page)
    return render(request,'event/upcoming.html',{'title':'upcoming','event':event})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.success(request, 'you are a member!')
                return redirect('signup')
        else:
            messages.info(request, 'password does not match')
            return redirect('signup')

    else:
        return render(request,'registration/signup.html',{'title':'signup'})


def profile(request):
    return render(request,'registration/userprofile.html',{'title':'profile'})