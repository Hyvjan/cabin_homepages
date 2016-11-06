from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from homepages.models import Reservation, Pictures
from homepages.forms import ReservationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def landing(request):
	return render_to_response('homepages/landing.html')

def booking(request):
	context=RequestContext(request)
	if request.method == 'POST':
		form = ReservationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			messages.add_message(request, messages.INFO, "Postauksesi on lisatty.")
			return HttpResponseRedirect('/booking')
		else:
			print form.errors
	else:
		form=ReservationForm()
	return render_to_response('homepages/booking.html', {'form':form}, context)

def lodge(request):
	pictures = Pictures.objects.all()
	return render_to_response('homepages/lodge.html',{'pictures':pictures}, RequestContext(request))

"""
def lodge(request):
	return render_to_response('homepages/lodge.html')
"""	