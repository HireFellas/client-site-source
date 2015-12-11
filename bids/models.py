from django.db import models
from jobs.models import UserProfile, QuoteRequest
from services.models import Photographer

# Create your models here.
class Bids(models.Model):
	user = models.ForeignKey(UserProfile)
	job = models.ForeignKey(QuoteRequest)
	photographer = models.ForeignKey(Photographer)
	quote_amount = models.IntegerField(default = 0)

	def __unicode__(self):
		return unicode(self.user.user.username)