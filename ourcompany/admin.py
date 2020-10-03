from django.contrib import admin
from .models import PastEvent,MeetupsEvent,WorkshopEvent,UpcomingEvent,LatestEvent,Profile


class PastEventAdmin(admin.ModelAdmin):
	list_display = ('title','facilitator','contact','date_created','venue')

class MeetupsEventAdmin(admin.ModelAdmin):
	list_display = ('title','facilitator','contact','date_created','venue')

class WorkshopEventAdmin(admin.ModelAdmin):
	list_display = ('title','facilitator','contact','date_created','venue')

class UpcomingEventAdmin(admin.ModelAdmin):
	list_display = ('title','facilitator','contact','date_created','venue')

class LatestEventAdmin(admin.ModelAdmin):
	list_display = ('title','facilitator','contact','date_created','venue')


admin.site.register(PastEvent,PastEventAdmin)
admin.site.register(LatestEvent,LatestEventAdmin)
admin.site.register(UpcomingEvent,UpcomingEventAdmin)
admin.site.register(WorkshopEvent,WorkshopEventAdmin)
admin.site.register(MeetupsEvent,MeetupsEventAdmin)
admin.site.register(Profile)
