from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from jobs.forms import QuoteForm
from jobs.models import UserProfile
#import sendgrid
import sys

# Create your views here.


def home(request):
	return render_to_response("jobs/home.html", RequestContext(request))

def contact(request):
	return render_to_response("static/contact.html", RequestContext(request))

def faq(request):
	return render_to_response("static/faq.html", RequestContext(request))

def terms(request):
	return render_to_response("static/terms.html", RequestContext(request))

def privacy(request):
	return render_to_response("static/privacy.html", RequestContext(request))

def team(request):
	return render_to_response("static/team.html", RequestContext(request))

def about(request):
	return render_to_response("static/about.html", RequestContext(request))

def success(request):
	return render_to_response("static/success.html", RequestContext(request))

def quoteForm(request):
	if request.method == 'POST':
		userprofile = UserProfile.objects.get(user=request.user)
		post_values = request.POST.copy()
		post_values['user'] = userprofile.user.id
		form = QuoteForm(post_values)
		print >> sys.stderr,  form.is_valid()
		if form.is_valid():
#			sg = sendgrid.SendGridClient('pranavprabhakar', 'W@lkinglif3+')
#			message = sendgrid.Mail()
#			message.add_to('HF <mail@hirefellas.com>')
#			message.set_subject('Quote Request')
#			userid = userprofile.user.username
#			message.set_text("You've a new quote request from " + userid)
#			message.set_from('Pranav Prabhakar <mail@hirefellas.com>')
#			status, msg = sg.send(message)
			form.save()
			return HttpResponseRedirect('/success/')
		else:
			print >> sys.stderr, form.errors
	else:
		form = QuoteForm()
		location = request.GET.get('location', '')
		#event_type = request.GET.get('event_type', '')
		photography_type = request.GET.get('photography_type', '')
		form.fields["location"].initial = location
		#form.fields["event_type"].initial = event_type
		form.fields["photography_type"].initial = photography_type
		print >> sys.stderr, photography_type
	return render(request, 'jobs/quote3.html', {'form': form})
