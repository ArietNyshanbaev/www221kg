from __future__ import unicode_literals
# imports form djagno
from django.shortcuts import render, render_to_response,redirect,get_object_or_404
from django.core.urlresolvers import reverse ,reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
#imports form model
from .models import Match, Bet, Tour, CurrentTour
from django.contrib.auth.models import User


# Create your views here.
def index(request):
	"""returns main page of bet app"""

	return render_to_response('bet/index.html',{},context_instance = RequestContext(request))

def archive(request):
	#define variables
	args = {}

	#getting data form models
	tours = Tour.objects.all()
    #do not include last ona because it has not result yet
	tours = tours[:len(tours)-1]

    #context data initialization into dictionary 'args'
	args['tours'] = tours

	return render_to_response('bet/archive.html',args,context_instance = RequestContext(request))

def tour_result(request,tourid):
	"""return rende results page for particular tour"""
	#define variables
	args = {}

    #if user is authenticated it gives extra information	
	if request.user.is_authenticated():
		user_bet = Bet.objects.filter(tour_number = tourid,user = request.user)
		if user_bet.count() == 1:
			args['user_bet'] = user_bet[0]
	
	#getting data form models
	bets = Bet.objects.filter(tour_number = tourid)
    #sort results by ranking of true results
	bets_temp = sorted(bets, key=lambda x: x.correct_num , reverse=True)

    #paginate 25 news per one page
	paginator = Paginator(bets_temp, 25)
	page = request.GET.get('page')
    
	try:
		bets_partial = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		bets_partial = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		bets_partial = paginator.page(paginator.num_pages)
    
    #context data initialization into dictionary 'args'
	args["bets_partial"] = bets_partial
	args['tour'] = tourid

	return render_to_response('bet/tour_result.html',args,context_instance = RequestContext(request))

def best_betters(request):
	"""returns best betters list with statistics"""
	#define variables
	args = {}
	results = {}
	keys = []
	#getting data form models
	tour_current = CurrentTour.objects.all()[0]
	if request.user.is_authenticated():
		user_result = {}
		average = 0
		bets = request.user.bet_set.all().exclude(tour_number = tour_current.tour_number)
		if bets.count() > 0:
			for bet in bets:
				average += bet.correct_num
			average = average / (bets.count())
			user_result[request.user.username] = average
			args['user_result'] = user_result

	#getting data form models
	users = User.objects.all().order_by('username')
	
	#get average for every user
	for user in users:
		average = 0
		bets = user.bet_set.all().exclude(tour_number = tour_current.tour_number)
		if bets.count() > 0:
			for bet in bets:
				average += bet.correct_num
			average = average / (bets.count())
			results[user.username] = average

	#context data initialization into dictionary 'args'
	args['results'] = results

	return render_to_response('bet/best_betters.html',args,context_instance = RequestContext(request))

def more_info(request,betid):
	"""returns page with more information of particular bet"""
	#define variables
	args = {}
	results = []
	statuses = []

	#getting data form models
	bet = get_object_or_404(Bet, pk = betid)
	tour = get_object_or_404(Tour, tour_number = bet.tour_number)
	matches = Match.objects.filter(tour = tour)
	
	#checking if user wins or loose in particular match
	if bet.match1 == 1:
		if matches[0].goal_first >  matches[0].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[0].first_team + ' победит')
	elif bet.match1 == 2:
		if matches[0].goal_first <  matches[0].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[0].second_team + ' победит')
	else:
		if matches[0].goal_first ==  matches[0].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match2 == 1:
		if matches[1].goal_first >  matches[1].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[1].first_team + ' победит')
	elif bet.match2 == 2:
		if matches[1].goal_first <  matches[1].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[1].second_team + ' победит')
	else:
		if matches[1].goal_first ==  matches[1].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match3 == 1:
		if matches[2].goal_first >  matches[2].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[2].first_team + ' победит')
	elif bet.match3 == 2:
		if matches[2].goal_first <  matches[2].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[2].second_team + ' победит')
	else:
		if matches[2].goal_first ==  matches[2].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match4 == 1:
		if matches[3].goal_first >  matches[3].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[3].first_team + ' победит')
	elif bet.match4 == 2:
		if matches[3].goal_first <  matches[3].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[3].second_team + ' победит')
	else:
		if matches[3].goal_first ==  matches[3].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match5 == 1:
		if matches[4].goal_first >  matches[4].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[4].first_team + ' победит')
	elif bet.match5 == 2:
		if matches[4].goal_first <  matches[4].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[4].second_team + ' победит')
	else:
		if matches[4].goal_first ==  matches[4].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match6 == 1:
		if matches[5].goal_first >  matches[5].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[5].first_team + ' победит')
	elif bet.match6 == 2:
		if matches[5].goal_first <  matches[5].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[5].second_team + ' победит')
	else:
		if matches[5].goal_first ==  matches[5].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match7 == 1:
		if matches[6].goal_first >  matches[6].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[6].first_team + ' победит')
	elif bet.match7 == 2:
		if matches[6].goal_first <  matches[6].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[6].second_team + ' победит')
	else:
		if matches[6].goal_first ==  matches[6].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match8 == 1:
		if matches[7].goal_first >  matches[7].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[7].first_team + ' победит')
	elif bet.match8 == 2:
		if matches[7].goal_first <  matches[7].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[7].second_team + ' победит')
	else:
		if matches[7].goal_first ==  matches[7].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match9 == 1:
		if matches[8].goal_first >  matches[8].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[8].first_team + ' победит')
	elif bet.match9 == 2:
		if matches[8].goal_first <  matches[8].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[8].second_team + ' победит')
	else:
		if matches[8].goal_first ==  matches[8].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')
	if bet.match10 == 1:
		if matches[9].goal_first >  matches[9].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[9].first_team + ' победит')
	elif bet.match10 == 2:
		if matches[9].goal_first <  matches[9].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append(matches[9].second_team + ' победит')
	else:
		if matches[9].goal_first ==  matches[9].goal_second:
			statuses.append(1)
		else:
			statuses.append(0)
		results.append('ничья')

	#context data initialization into dictionary 'args'
	args['statuses'] = statuses
	args['results'] = results
	args['bet'] = bet
	args['matches'] = matches
	return render_to_response('bet/more_info.html',args,context_instance = RequestContext(request))

@login_required(login_url=reverse_lazy('main:signin'))
def check(request,tourid):
	"""this view does something """

	if request.user == User.objects.get(username = 'ariet'):
		#getting data form models
	    bets = Bet.objects.filter(tour_number = tourid)
	    matches = Match.objects.filter(tour = tourid)

	    #check if user made a true or wrong guess
	    for bet in range(0,len(bets)):
	        counter = 0 
	        if matches[0].goal_first >  matches[0].goal_second:
	        	if bets[bet].match1 == 1:
	        		counter += 1
	        elif matches[0].goal_first <  matches[0].goal_second:
	        	if bets[bet].match1 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match1 == 3:
	        		counter += 1

	        if matches[1].goal_first >  matches[1].goal_second:
	        	if bets[bet].match2 == 1:
	        		counter += 1
	        elif matches[1].goal_first <  matches[1].goal_second:
	        	if bets[bet].match2 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match2 == 3:
	        		counter += 1

	        if matches[2].goal_first >  matches[2].goal_second:
	        	if bets[bet].match3 == 1:
	        		counter += 1
	        elif matches[2].goal_first <  matches[2].goal_second:
	        	if bets[bet].match3 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match3 == 3:
	        		counter += 1

	        if matches[3].goal_first >  matches[3].goal_second:
	        	if bets[bet].match4 == 1:
	        		counter += 1
	        elif matches[3].goal_first <  matches[3].goal_second:
	        	if bets[bet].match4 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match4 == 3:
	        		counter += 1

	        if matches[4].goal_first >  matches[4].goal_second:
	        	if bets[bet].match5 == 1:
	        		counter += 1
	        elif matches[4].goal_first <  matches[4].goal_second:
	        	if bets[bet].match5 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match5 == 3:
	        		counter += 1

	        if matches[5].goal_first >  matches[5].goal_second:
	        	if bets[bet].match6 == 1:
	        		counter += 1
	        elif matches[5].goal_first <  matches[5].goal_second:
	        	if bets[bet].match6 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match6 == 3:
	        		counter += 1

	        if matches[6].goal_first >  matches[6].goal_second:
	        	if bets[bet].match7 == 1:
	        		counter += 1
	        elif matches[6].goal_first <  matches[6].goal_second:
	        	if bets[bet].match7 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match7 == 3:
	        		counter += 1

	        if matches[7].goal_first >  matches[7].goal_second:
	        	if bets[bet].match8 == 1:
	        		counter += 1
	        elif matches[7].goal_first <  matches[7].goal_second:
	        	if bets[bet].match8 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match8 == 3:
	        		counter += 1

	        if matches[8].goal_first >  matches[8].goal_second:
	        	if bets[bet].match9 == 1:
	        		counter += 1
	        elif matches[8].goal_first <  matches[8].goal_second:
	        	if bets[bet].match9 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match9 == 3:
	        		counter += 1

	        if matches[9].goal_first >  matches[9].goal_second:
	        	if bets[bet].match10 == 1:
	        		counter += 1
	        elif matches[9].goal_first <  matches[9].goal_second:
	        	if bets[bet].match10 == 2:
	        		counter += 1
	        else:
	        	if bets[bet].match10 == 3:
	        		counter += 1
	        bets[bet].correct_num = counter
	        bets[bet].save()

	return redirect(reverse('bet:index'))


def make_bet(request):
	"""this view handles making bet"""
	#define variables
	args={}
	args.update(csrf(request))
	valid = True

	if request.POST:
		user = request.user
		statuses = request.POST.getlist('status')

        #if form haven't been filled corretly
		if len(statuses) < 10:
			status_error = "Заполните все поля"
			valid = False
			args['status_error'] = status_error
        #if form have been filled correctly
		else:
			match1 = int(statuses[0])
			match2 = int(statuses[1])
			match3 = int(statuses[2])
			match4 = int(statuses[3])
			match5 = int(statuses[4])
			match6 = int(statuses[5])
			match7 = int(statuses[6])
			match8 = int(statuses[7])
			match9 = int(statuses[8])
			match10 = int(statuses[9])

	    #getting data form models
		tour_current = CurrentTour.objects.all()[0]
		tour_of_bet = tour_current.tour_number

        #if we got validation error
		if valid == False:
        	#getting data form models
			tour_to_use = get_object_or_404(Tour, pk = tour_current.tour_number)
			bets = Match.objects.filter(tour = tour_to_use)
            #context data initialization into dictionary 'args'
			args['tour'] = tour_to_use
			args['bets'] = bets

			return render_to_response('bet/betform.html',args,context_instance = RequestContext(request))
        
        #create an inctance of model if everything is valid
		bet = Bet.objects.create(user=user,tour_number = tour_of_bet,match1=match1,match2=match2,match3=match3,match4=match4,match5=match5,match6=match6,match7=match7,match8=match8,match9=match9,match10=match10)
		bet.full_clean()
		bet.save()

        #getting data form models
		tour = CurrentTour.objects.all()[0]
		bets_of_user = Bet.objects.all().filter(user=request.user,tour_number = tour.tour_number)
        #if user have bet collect the data about bet
		if bets_of_user.count() > 0:
			bet_of_user = bets_of_user[0]
			list_of_matches = []
			list_of_matches.append(bet_of_user.match1)
			list_of_matches.append(bet_of_user.match2)
			list_of_matches.append(bet_of_user.match3)
			list_of_matches.append(bet_of_user.match4)
			list_of_matches.append(bet_of_user.match5)
			list_of_matches.append(bet_of_user.match6)
			list_of_matches.append(bet_of_user.match7)
			list_of_matches.append(bet_of_user.match8)
			list_of_matches.append(bet_of_user.match9)
			list_of_matches.append(bet_of_user.match10)

        	#getting data form models
			tour_to_use = get_object_or_404(Tour, pk = tour.tour_number)
			bets = Match.objects.filter(tour = tour_to_use)
			bets = zip(bets, list_of_matches)
			#context data initialization into dictionary 'args'
			args['bets'] = bets
			args['tour'] = tour_to_use
			args['bet_of_user'] = bet_of_user
			args['success_message'] = "Вы успешно сделали ставку"

		return render_to_response('bet/betform.html',args,context_instance = RequestContext(request))

	else:
		#getting data form models
		tour = CurrentTour.objects.all()[0]
		if request.user.is_authenticated():
    		#getting data form models
			bets_of_user = Bet.objects.all().filter(user=request.user,tour_number = tour.tour_number)
			#if user has any bet collect information about that bet
			if bets_of_user.count() > 0:
				bet_of_user = bets_of_user[0]
				list_of_matches = []
				list_of_matches.append(bet_of_user.match1)
				list_of_matches.append(bet_of_user.match2)
				list_of_matches.append(bet_of_user.match3)
				list_of_matches.append(bet_of_user.match4)
				list_of_matches.append(bet_of_user.match5)
				list_of_matches.append(bet_of_user.match6)
				list_of_matches.append(bet_of_user.match7)
				list_of_matches.append(bet_of_user.match8)
				list_of_matches.append(bet_of_user.match9)
				list_of_matches.append(bet_of_user.match10)
				#getting data form models
				tour_to_use = get_object_or_404(Tour, pk = tour.tour_number)
				bets = Match.objects.filter(tour = tour_to_use)
				bets = zip(bets, list_of_matches)
				#context data initialization into dictionary 'args'
				args['bets'] = bets
				args['tour'] = tour_to_use
				args['bet_of_user'] = bet_of_user
			else:
				tour_to_use = Tour.objects.get(pk=tour.tour_number)
				bets = Match.objects.filter(tour = tour_to_use)
				args['bets'] = bets
				args['tour'] = tour_to_use
		else:
			#getting data form models
			tour_to_use = get_object_or_404(Tour, pk = tour.tour_number)
			bets = Match.objects.filter(tour = tour_to_use)
			#context data initialization into dictionary 'args'
			args['bets'] = bets
			args['tour'] = tour_to_use
		return render_to_response('bet/betform.html',args,context_instance = RequestContext(request))

def team(request):
	"""retruns rendered team page"""
	# define variables
	args={}
	if request.user.is_authenticated():
		args["user"] = request.user
		
	return render_to_response('bet/team.html',args,context_instance = RequestContext(request))

def how_it_works(request):
	"""returns rendered information how does bet app works"""
	# define variables
	args = {}
	if request.user.is_authenticated():
		args["user"] = request.user

	return render_to_response('bet/how_it_works.html',args)
