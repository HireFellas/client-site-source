from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
 
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
	    fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
	 
	    if len(fb_uid):
	        return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
	 
	    return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

class QuoteRequest(models.Model):
	user = models.ForeignKey(UserProfile, null=True)
	location = models.CharField(max_length=25, default= 'Chennai')
	#event_type = models.CharField(max_length=25, default = 'Photography')
	photography_type = models.CharField(max_length=25, default = 'Wedding')
	no_people_choices = (('1', 'Less than 50 people'),('2','50 to 100 people'),('3','100 to 200 people'),('4','200 to 500 people'),('5','More than 500 people'),)
	no_people = models.CharField(max_length=1,choices=no_people_choices,default=None, null = True)
	event_date = models.DateField('Event Date', default=datetime.now().date())
	event_venue_choices = (('1', 'Indoors'),('2','Outdoors'),('3',"I'm not sure yet"),)
	event_venue = models.CharField(max_length=1,choices=event_venue_choices,default=None, null = True)
	deliverables_choices = (
		('1', 'CD/DVD'),
		('2','Online Download'),
		('3',"Physical Prints"),
	)
	deliverables = models.CharField(max_length=1,choices=deliverables_choices,default=None,  null = True)
	budget_choices = (
	('1', 'Less than INR 15,000'),
	('2','INR 15,000 to 30,000'),
	('3','INR 30,000 to 60,000'),
	('4','INR 60,000 to 1,00,000'),
	('5','More than 1,00,000'),
	)
	budget = models.CharField(max_length=1,choices=budget_choices,default='Less than INR 15,000',  null = False)
	details = models.TextField(null = True)

	class Meta:
		db_table = 'quote_request'

	def __unicode__(self):
		return unicode(self.id)



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])