from django.db import models
from django.contrib.auth.models import User

#profile model
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return f'{self.user.username}'


#model-1  past_event model
class PastEvent(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='past_pics')
    description = models.TextField()
    contact = models.CharField(max_length=16)
    facilitator = models.CharField(max_length=55)
    date_created = models.DateTimeField()
    venue = models.CharField(max_length=55)
    def __str__(self):
        return self.title

#model2 latest_event model
class LatestEvent(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='latest_pics')
    description = models.TextField()
    contact = models.CharField(max_length=16)
    facilitator = models.CharField(max_length=55)
    date_created = models.DateTimeField()
    venue = models.CharField(max_length=55)
    def __str__(self):
        return self.title

#model3 upcoming_event model
class UpcomingEvent(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='upcoming_pics')
    description = models.TextField()
    contact = models.CharField(max_length=16)
    facilitator = models.CharField(max_length=55)
    date_created = models.DateTimeField()
    venue = models.CharField(max_length=55)
    def __str__(self):
        return self.title

#model4 workshops_event model
class WorkshopEvent(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='workshops_pics')
    description = models.TextField()
    contact = models.CharField(max_length=16)
    facilitator = models.CharField(max_length=55)
    date_created = models.DateTimeField()
    venue = models.CharField(max_length=55)
    def __str__(self):
        return self.title

#model5 meetups_event model
class MeetupsEvent(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='meetups_pics')
    description = models.TextField()
    contact = models.CharField(max_length=16)
    facilitator = models.CharField(max_length=55)
    date_created = models.DateTimeField()
    venue = models.CharField(max_length=55)
    def __str__(self):
        return self.title
