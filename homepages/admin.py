import django_bootstrap_calendar
from django.contrib import admin
from django_bootstrap_calendar.models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "css_class", "start", "end"]
    list_filler = ["title"]

admin.site.register(CalendarEvent, CalendarEventAdmin)
