#import of django
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse , reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#impoer of models 
from .models import Information
from django.contrib.auth.models import User


# Create your views here.

def main(request):
	
	return render_to_response('main/main.html',{})

def team(request):
	args={}
	
	if request.user.is_authenticated():
		args["user"] = request.user
	return render_to_response('main/team.html',args)

def signin(request,key = 'main'):
	if request.user.is_authenticated():
		return redirect(reverse("main:main"))
	args={}
	args.update(csrf(request))

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				args['user'] = user
				if key == 'bet':
					return redirect(reverse('bet:index'))
				if key == 'reservation':
					return redirect(reverse('reservation:index'))
				if key == 'main':
					return redirect(reverse('main:main'))
			else:
				args['error_message'] = "Ваш аккаунт временно заблокирован"
				return render_to_response('main/signin.html',args)
		else:
			args['error_message'] = "Имя пользователя и пароль не совпадают, попробуйте еще раз. "
			return render_to_response('main/signin.html',args)

	else:
		return render_to_response('main/signin.html',args)

def signup(request):
	if request.user.is_authenticated():
		return redirect(reverse("main:main"))

	args={}
	args.update(csrf(request))
	validation = True
	all_users = User.objects.all()
	if request.POST:
		first_name = request.POST.get('first_name','')
		last_name = request.POST.get('last_name','')
		phone_num = request.POST.get('phone_num','')
		username = request.POST.get('username','')
		email = request.POST.get('e_mail','')
		password1 = request.POST.get('password1','')
		password2 = request.POST.get('password2','')

		#field validation:
		#first_name validation
		if len(first_name) < 2 :
			args['first_name_error'] = 'Слишком короткое имя'
			validation = False
		else:
			args['first_name'] = first_name
		if len(last_name) < 2 :
		#last_name validation
			args['last_name_error'] = 'Слишком короткая фамилия'
			validation = False
		else:
			args['last_name'] = last_name
		#phone_number validation
		if len(phone_num) != 10:
			validation = False
			args['phone_num_error'] = "Пожайлуста введите номер телефона в правилном 10 значном формате например : (0555123456)"
		else:
			phone_valid = True
			for i in phone_num:
				if ord(i) > 57 or ord(i) < 48:
					phone_valid = False
					break
			if phone_valid :
				if_number_in_use = Information.objects.filter(phone_number=phone_num[1:])
				if if_number_in_use.count() > 0: 
					args['phone_num_error'] = "Этот номер уже используется"
				else:
					args['phone_num'] = phone_num
			else:
				validation = False
				args['phone_num_error'] = "Пожайлуста введите номер телефона правилно например : (0555123456)"
		#username validation
		if len(username) > 2:
			users_using_thisname = all_users.filter(username__iexact=username)
			if users_using_thisname.count() > 0:
				validation = False
				args['username_error'] = 'Этот логин уже используется'
			else:
				args['username'] = username
		else:
			args['username_error'] = 'Слишком короткий логин'

		#password validation
		if len(password1) < 6 or len(password2) < 6:
			validation = False
			args['password_error'] = 'Пароль должен состоять из 6 и более символов'

		#email validation
		users_using_email = all_users.filter(email=email)
		if users_using_email.count() > 0:
			validation = False
			args['email_error'] = 'Этот email уже зарегистрирован' 
		else:
			args['email'] = email

		if validation == False:
			return render_to_response('main/signup.html', args)

		if password1 == password2:
			user = User.objects.create_user(username = username, email = email, password = password1)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			information = Information.objects.create(user = user, phone_number = phone_num,can_book = False)
			information.save()
			return redirect(reverse('main:signin'))
		else:
			args['email'] = email
			args['password_error'] = 'Пароли не совпадают'
			return render_to_response('main/signup.html', args)

	else:
		return render_to_response('main/signup.html',args)

def signout(request):
	logout(request)
	return redirect(reverse('main:main'))

@login_required(login_url=reverse_lazy('main:signin'))
def profile(request):
	args = {}
	user = request.user
	args['user'] = user
	return render_to_response('main/profile.html',args)

@login_required(login_url=reverse_lazy('main:signin'))
def modify_profile(request):
	args = {}
	args.update(csrf(request))
	validation = True
	user = request.user

	if request.POST:
		first_name = request.POST.get('firstname','')
		last_name = request.POST.get('lastname','')
		email = request.POST.get('email','')

		#field validation:
		#first_name validation
		if len(first_name) < 2 :
			args['first_name_error'] = 'Слишком короткое имя'
			validation = False

		if len(last_name) < 2 :
		#last_name validation
			args['last_name_error'] = 'Слишком короткая фамилия'
			validation = False

		users_using_email = User.objects.all().filter(email=email)
		if users_using_email.count() > 0:
			args['email_error'] = 'Этот email уже зарегистрирован'
			validation = False

		if validation == False:
			args['user'] = user
			return render_to_response('main/modify_profile.html', args)

		user.email = email
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		return redirect(reverse('main:profile'))
	else:
		args['user'] = user
		return render_to_response('main/modify_profile.html',args)

@login_required(login_url=reverse_lazy('main:signin'))
def change_password(request):
	args = {}
	args.update(csrf(request))
	user = request.user
	args['user'] = user
	if request.POST:
		password1 = request.POST.get('password1','')
		password2 = request.POST.get('password2','')

		if len(password1) < 6 or len(password2) < 6:
			args['password_error'] = 'Пароль должен состоять из 6 и более символов'
			return render_to_response('main/change_password.html',args)
		if password1 == password2:
			user.set_password(password1)
			user.save()
			args['success_message'] = 'Ваш пароль успешно изменен'
		else:
			args['password_error'] = 'Пароли не совпадают'
		return render_to_response('main/change_password.html',args)
	else:
		return render_to_response('main/change_password.html',args)


