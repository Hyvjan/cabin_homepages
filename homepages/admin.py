import django_bootstrap_calendar
from django.contrib import admin
from django_bootstrap_calendar.models import CalendarEvent
from homepages.models import Reservation, Pictures, NaturePictures

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "css_class", "start", "end"]
    list_filler = ["title"]

admin.site.register(CalendarEvent, CalendarEventAdmin)

class ReservationAdmin(admin.ModelAdmin):
    reservation_display = ['arrival_date', 'end_date', 'first_name', 'last_name', 
		'email', 'phone_number', 'message']
    reservation_filler = ["arrival_date"]

admin.site.register(Reservation, ReservationAdmin)

class PicturesAdmin(admin.ModelAdmin):
    pictures_display = ['picture', 'file_up']
    picture_filler = ["picture"]

admin.site.register(Pictures, PicturesAdmin)

class NaturePicturesAdmin(admin.ModelAdmin):
    pictures_display = ['picture_description', 'file_up']
    picture_filler = ["picture_descrition"]

admin.site.register(NaturePictures, NaturePicturesAdmin)