from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from bids.models import Bids
from jobs.models import UserProfile
# Create your views here.
def listBids(request):
	userprofile = UserProfile.objects.get(user=request.user)
	total_bids = Bids.objects.filter(user = userprofile.user.id)
	return render(request, 'bids/bids3.html', {'bids': total_bids})

