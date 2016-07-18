from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import EnterDetail
from django.shortcuts import render

#CheckAvailability
from .forms import Details
import datetime

class IndexView(generic.ListView):
    '''
    To have a button for 'BOOK AN APPOINTMENT'!!
    '''

    model=EnterDetail
    template_name='appschedule/index.html'
    #pk=enterDetail_list.id
    #def get(request,enterDetail_id):
        
    
    #   enterDetail=get_object_or_404(EnterDetail,pk=enterDetail_id)
        
    #context_object_name='details'
    #def get_queryset(self):
     #   return SelectDateTime.objects.order_by('-date_time')
    
class DetailView(generic.FormView):
    '''
    To fill in details for booking!!
    '''

    model=EnterDetail
    form_class=Details
    template_name='appschedule/detail.html'
    '''try:
        context={ 'already_booked':ResultView.already_booked , 'vacant' : ResultView.vacant }
    except NameError:
        pass'''
'''    def get_queryset(self):
        time_slots=[9,10,11,12,2,3,4]
        lunch_time=[1]
        return
'''
class ResultView(generic.View):
    '''
    To print confirmation of appointment or redirect with an error back to detail view!!
    ''' 
    #model=EnterDetail
    form_class=Details
    template_name='appschedule/results.html'
    #model=CheckAvailability
    def post(self,request):
        form=self.form_class(request.POST)
    #if request.method=='POST':
        #form=Detail(request.POST)
        if form.is_valid():
            #reads data from form
            formname   =form.cleaned_data['name']
            formcontact=form.cleaned_data['contact_no']
            formage    =form.cleaned_data['age']
            formdate   =form.cleaned_data['date']
            formtime   =form.cleaned_data['time']
            #formtime=form.cleaned_data['time']
            #matches form data with database

            if EnterDetail.objects.filter(date=formdate,time=formtime).exists():
                error_message='This slot has already been Booked!'
                already_booked_time=EnterDetail.objects.filter(date=formdate).values_list('time',flat=True).order_by('time')
                already_booked=[tt.strftime('%H:%M') for tt in already_booked_time]
                vacant=[]
                for index in range(len(Details.CHOICES)):
                    t=Details.CHOICES[index][1]
                    if t not in already_booked:
                        vacant.append(t)
                #already_booked=[tt.strftime('%H:%M') for tt in already_booked_time]     
                return render(request,self.template_name,{'form':form,'error_message':error_message,'already_booked':already_booked,'vacant':vacant})
            
            else:
                particulars=EnterDetail.objects.create(name=formname,contact_no=formcontact,age=formage,date=formdate,time=formtime)
                particulars.save()
                ########print CheckAvailability.objects.filter(date=formdate).exclude(time)
                return render(request,self.template_name,{'form':form})
                


        #obj_chk.chkifbooked=='not booked'
        #then add entry and redirect to results.html with a positive confirmation
        #else show an ERROR MESSAGE on confirmation page and the 'not booked' slots for that day also a button to redirect to details.html
        #save to database using form.save()
        
    #now we need to add the time to database if the slot the empty else print an error message and a submit #button to redirect back to DetailView