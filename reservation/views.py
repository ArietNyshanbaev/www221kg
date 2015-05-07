#imports form django libraries
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse ,reverse_lazy
from django.template import RequestContext
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
#imports from models
from .models import Day, Field,BookRequest
#imports from 3-rd party libraries
import requests

# Create your views here.
def index(request):
	"""returns reservation manin page"""

	return render_to_response('reservation/index.html', {}, context_instance = RequestContext(request))

def team(request):
	"""returns rendered our team page"""

	return render_to_response('reservation/team.html', {}, context_instance = RequestContext(request))

def schedule(request,field_id = 1):
	"""shows the schedule for particular field"""
	#define variables
	args = {}
	hours = []
	#getting data form models
	field = get_object_or_404(Field, pk = field_id)
	days = field.day_set.all() 
	
	#gettin hours to show
	for i in range(9,24):
		hours += [i]	
	#context data initialization into dictionary 'args'
	args['field'] = field
	args['hours'] = hours
	args['days'] = days

	return render_to_response('reservation/schedule.html',args,context_instance = RequestContext(request))

def list(request):
	"""this view shows the list of all fields as a list"""
	#define variables
	args = {}
	#gettin hours to show
	fields = Field.objects.all()
	#context data initialization into dictionary 'args'
	args['fields'] = fields

	return render_to_response('reservation/list.html',args,context_instance = RequestContext(request))

def reserve(request,field_id,day_id):
	"""this view is manipulates fields hours"""
	#define variables
	args={}
	args.update(csrf(request))
	message = "Chislo : "
	hours1 = []
	hours2 = []

	for i in range(9,17):
		hours1 += [i]
	for i in range(17,25):
		hours2 += [i]

	if request.POST:
		#gettin hours to show
		user = request.user
		date_time = get_object_or_404(Day, pk = day_id).date
		field = get_object_or_404(Field, pk = field_id)
		allhours = request.POST.getlist('hour')
		begin_time = ''
		
		for hour in allhours:
			begin_time = begin_time + (hour + ', ')


		valid = True
		if len(allhours) < 2:
			valid = False
			hour_error = "Выберите время не менее одного часа"
			args['hour_error'] = hour_error

		if valid ==  False:
			#context data initialization into dictionary 'args'
			args['field'] = get_object_or_404(Field, pk = field_id)
			args['hours1'] = hours1
			args['hours2'] = hours2
			args['day'] = get_object_or_404(Day, pk = day_id)

			return render_to_response('reservation/reserve.html',args,context_instance = RequestContext(request))

		bookRequest = BookRequest.objects.create(user=user,time = allhours,date_time=date_time,field=field)
		bookRequest.full_clean()
		
		day = get_object_or_404(Day, pk = day_id)
		
		for hour in allhours:
			
			if hour == '09-00':
				day.h9_00 = True
			if hour == '09-30':
				day.h9_30 = True
			if hour == '10-00':
				day.h10_00 = True
			if hour == '10-30':
				day.h10_30 = True
			if hour == '11-00':
				day.h11_00 = True
			if hour == '11-30':
				day.h11_30 = True
			if hour == '12-00':
				day.h12_00 = True
			if hour == '12-30':
				day.h12_30 = True
			if hour == '13-00':
				day.h13_00 = True
			if hour == '13-30':
				day.h13_30 = True
			if hour == '14-00':
				day.h14_00 = True
			if hour == '14-30':
				day.h14_30 = True
			if hour == '15-00':
				day.h15_00 = True
			if hour == '15-30':
				day.h15_30 = True
			if hour == '16-00':
				day.h16_00 = True
			if hour == '16-30':
				day.h16_30 = True
			if hour == '17-00':
				day.h17_00 = True
			if hour == '17-30':
				day.h17_30 = True
			if hour == '18-00':
				day.h18_00 = True
			if hour == '18-30':
				day.h18_30 = True
			if hour == '19-00':
				day.h19_00 = True
			if hour == '19-30':
				day.h19_30 = True
			if hour == '20-00':
				day.h20_00 = True
			if hour == '20-30':
				day.h20_30 = True
			if hour == '21-00':
				day.h21_00 = True
			if hour == '21-30':
				day.h21_30 = True
			if hour == '22-00':
				day.h22_00 = True
			if hour == '22-30':
				day.h22_30 = True
			if hour == '23-00':
				day.h23_00 = True
			if hour == '23-30':
				day.h23_30 = True
			if hour == '24-00':
				day.h24_00 = True
			if hour == '24-30':
				day.h24_30 = True
		
		day.full_clean()
		
		message +=  str(day.date) + "\nzabranirovano : "

		message += ', '.join(allhours)

		sms_url = 'http://smsc.ru/sys/send.php?login=traktorist221&psw=smsc120701&phones=996556606737&mes='
		message += '\nfrom 221.kg'
		sms_url += message
		#send sms by httpget
		r = requests.get(sms_url)
		

		#save inctances to the db
		day.save()
		bookRequest.save()
		field = get_object_or_404(Field, pk = field_id)
		#send_mail(subject,message,from_email,to_list,fail_silently=False)
		message_body = 'Вы забронировали ' + field.name + ' \n дата: ' + str(day.date) + '\n время: (' + ', '.join(allhours) + ')' + '\n + желаем вам приятной игры'
		send_mail('Бронирование 221', message_body, settings.EMAIL_HOST_USER, [user.email], fail_silently = True)
		#context data initialization into dictionary 'args'
		args['field'] = field
		args['hours1'] = hours1
		args['hours2'] = hours2
		args['day'] = get_object_or_404(Day, pk = day_id)
		args['success_message'] = "вы успешно забронировали поле (" + ', '.join(allhours) + ")"

		return render_to_response('reservation/reserve.html',args,context_instance = RequestContext(request))

	else:
		#context data initialization into dictionary 'args'
		args['field'] = get_object_or_404(Field,pk = field_id)
		args['hours1'] = hours1
		args['hours2'] = hours2
		args['day'] = get_object_or_404(Day, pk = day_id)

		return render_to_response('reservation/reserve.html',args,context_instance = RequestContext(request))