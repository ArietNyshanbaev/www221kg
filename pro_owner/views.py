#import of django
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse , reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#impoer of models 
from django.contrib.auth.models import User
from reservation.models import Field, Day

# Create your views here.

# signin only for owners of fields
def signin_as_owner(request):
	args={}
	args.update(csrf(request))

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				if user.field_set.all().count() > 0:
					login(request, user)
					return redirect(reverse('pro_owner:home'))
				else:
					args['error_message'] = "У вас нет доступа к этой странице. "
					return render_to_response('pro_owner/signin_as_owner.html',args)
			else:
				args['error_message'] = "Ваш аккаунт временно заблокирован"
				return render_to_response('pro_owner/signin_as_owner.html',args)
		else:
			args['error_message'] = "Имя пользователя и пароль не совпадают, попробуйте еще раз. "
			return render_to_response('pro_owner/signin_as_owner.html',args)

	else:
		return render_to_response('pro_owner/signin_as_owner.html',args)

@login_required(login_url=reverse_lazy('pro_owner:signin_as_owner'))
def home(request):
	args={}
	user = request.user
	if user.field_set.all().count() < 1:
		return redirect(reverse('pro_owner:signin_as_owner'))

	args['fields'] = user.field_set.all()
	args['user'] = user
	return render_to_response('pro_owner/home.html', args)

@login_required(login_url=reverse_lazy('pro_owner:signin_as_owner'))
def info_field(request,field_id):
	args={}
	user = request.user
	field = get_object_or_404(Field,pk=field_id)
	args['field'] = field
	args['user'] = user
	if not field.owner == user:
		return redirect(reverse('pro_owner:signin_as_owner'))

	return render_to_response('pro_owner/info_field.html', args)

@login_required(login_url=reverse_lazy('pro_owner:signin_as_owner'))
def info_day(request,field_id, day_id):
	args={}
	args.update(csrf(request))
	user = request.user
	field = get_object_or_404(Field,pk=field_id)

	if not field.owner == user:
		return redirect(reverse('pro_owner:signin_as_owner'))
	day = get_object_or_404(Day, pk=day_id)
	args['day'] = day
	args['field'] = field
	args['user'] = user

	if request.POST:
		allhours = request.POST.getlist('hour')
		
		if '09-00' in allhours:
			day.h9_00 = True
		else:
			day.h9_00 = False
		if '09-30' in allhours:
			day.h9_30 = True
		else:
			day.h9_30 = False
		if '10-00' in allhours:
			day.h10_00 = True
		else:
			day.h10_00 = False
		if '10-30' in allhours:
			day.h10_30 = True
		else:
			day.h10_30 = False
		if '11-00' in allhours:
			day.h11_00 = True
		else:
			day.h11_00 = False
		if '11-30' in allhours:
			day.h11_30 = True
		else:
			day.h11_30 = False
		if '12-00' in allhours:
			day.h12_00 = True
		else:
			day.h12_00 = False
		if '12-30' in allhours:
			day.h12_30 = True
		else:
			day.h12_30 = False
		if '13-00' in allhours:
			day.h13_00 = True
		else:
			day.h13_00 = False
		if '13-30' in allhours:
			day.h13_30 = True
		else:
			day.h13_30 = False
		if '14-00' in allhours:
			day.h14_00 = True
		else:
			day.h14_00 = False
		if '14-30' in allhours:
			day.h14_30 = True
		else:
			day.h14_30 = False
		if '15-00' in allhours:
			day.h15_00 = True
		else:
			day.h15_00 = False
		if '15-30' in allhours:
			day.h15_30 = True
		else:
			day.h15_30 = False
		if '16-00' in allhours:
			day.h16_00 = True
		else:
			day.h16_00 = False
		if '16-30' in allhours:
			day.h16_30 = True
		else:
			day.h16_30 = False
		if '17-00' in allhours:
			day.h17_00 = True
		else:
			day.h17_00 = False
		if '17-30' in allhours:
			day.h17_30 = True
		else:
			day.h17_30 = False
		if '18-00' in allhours:
			day.h18_00 = True
		else:
			day.h18_00 = False
		if '18-30' in allhours:
			day.h18_30 = True
		else:
			day.h18_30 = False
		if '19-00' in allhours:
			day.h19_00 = True
		else:
			day.h19_00 = False
		if '19-30' in allhours:
			day.h19_30 = True
		else:
			day.h19_30 = False
		if '20-00' in allhours:
			day.h20_00 = True
		else:
			day.h20_00 = False
		if '20-30' in allhours:
			day.h20_30 = True
		else:
			day.h20_30 = False
		if '21-00' in allhours:
			day.h21_00 = True
		else:
			day.h21_00 = False
		if '21-30' in allhours:
			day.h21_30 = True
		else:
			day.h21_30 = False
		if '22-00' in allhours:
			day.h22_00 = True
		else:
			day.h22_00 = False
		if '22-30' in allhours:
			day.h22_30 = True
		else:
			day.h22_30 = False
		if '23-00' in allhours:
			day.h23_00 = True
		else:
			day.h23_00 = False
		if '23-30' in allhours:
			day.h23_30 = True
		else:
			day.h23_30 = False
		if '24-00' in allhours:
			day.h24_00 = True
		else:
			day.h24_00 = False
		if '24-30' in allhours:
			day.h24_30 = True
		else:
			day.h24_30 = False
		day.save()


	return render_to_response('pro_owner/info_day.html',args)

