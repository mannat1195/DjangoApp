from django import forms
import datetime

class Details(forms.Form):
    CHOICES=[('09:00 am','09:00'),('10:00 am','10:00'),('11:00 am','11:00'),('12:00 noon','12:00'),('2:00 pm','2:00'),('3:00 pm','3:00'),('4:00 pm','4:00'), ]
    name=forms.CharField(max_length=100)
    age=forms.CharField(max_length=5)
    contact_no=forms.CharField(max_length=15)
    date=forms.DateField(widget=forms.SelectDateWidget())    
    time=forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    
   