from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext

# Create your views here.
def booking(request):
	return render_to_response('homepages/booking.html', RequestContext(request))