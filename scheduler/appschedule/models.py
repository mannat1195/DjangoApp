import datetime
from django.db import models
# Create your models here.

class EnterDetail(models.Model):
	#inputs provided by the user
	name=models.CharField(max_length=100)
	age=models.CharField(max_length=5)
	contact_no=models.CharField(max_length=15)
	date=models.DateField()
	time=models.TimeField()
	
	def __str__(self):
		return self.name
	
#class CheckAvailability(models.Model):
#	dt=models.ForeignKey(EnterDetails,on_delete=models.CASCADE)
	#chkifbooked=models.CharField(max_length=100,default='not booked')
	# chk_if_available=CharField(max_length=100)
	#if datetime.time==booked:
'''
	
class Book(models.Model):
	bookanotherslot=CharField(max_length=100)
	confirmation=CharField(max_length=100)
	
	def __str__(self):
		return(self.bookanotherslot,self.confirmation)
'''