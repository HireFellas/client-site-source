from django.forms import ModelForm
from jobs.models import QuoteRequest, UserProfile
from django import forms

class QuoteForm(ModelForm):
	user = forms.ModelChoiceField(queryset=UserProfile.objects.all(), widget=forms.HiddenInput())
	details = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = QuoteRequest
		fields = ['user',
		'location',
		#'event_type',
		'photography_type',
		'no_people',
		'event_date',
		'event_venue',
		'deliverables',
		'details',
		'budget']
