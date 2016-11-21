from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from homepages.models import Reservation, Pictures,NaturePictures
from homepages.forms import ReservationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from kaunisvilla import settings
from django.core.mail import send_mail

# Create your views here.

def landing(request):
	return render_to_response('homepages/landing.html')

def booking(request):
	context=RequestContext(request)
	if request.method == 'POST':
		form = ReservationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			messages.add_message(request, messages.INFO, "Your booking request has been sent. Thank You.")
			arrival_date = form.cleaned_data['arrival_date']
			end_date = form.cleaned_data['end_date']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			viesti = "{}+:+{}+:+{}+:+{}+:+{}+:+{}".format(arrival_date,end_date,first_name.encode('utf-8'),last_name.encode('utf-8'),email.encode('utf-8'),message.encode('utf-8'))
			send_mail('Varauspyynto Kaunisvillaan', viesti, settings.EMAIL_HOST_USER,
         	['janne.j.hyvonen@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/booking')
		else:
			print form.errors
	else:
		form=ReservationForm()
	return render_to_response('homepages/booking.html', {'form':form}, context)

def lodge(request):
	pictures = Pictures.objects.all()
	return render_to_response('homepages/lodge.html',{'pictures':pictures}, RequestContext(request))

def activities(request):
	return render_to_response('homepages/activities.html')

def terms(request):
	return render_to_response('homepages/terms.html')

def nature(request):
	pictures_nature = NaturePictures.objects.all()
	return render_to_response('homepages/nature.html',{'pictures_nature':pictures_nature}, RequestContext(request))
