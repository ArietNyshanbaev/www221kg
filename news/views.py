#importing django libraries
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse ,reverse_lazy
#importing models
from news.models import League,Team,News
#importing form python libraries
from datetime import datetime 


def index(request):
	"""returns rendered main page of news app"""

	#define variables
	args = {}
	all_teams = []
	all_news = []
	
	#getting data form models
	leagues = League.objects.all()
	
	#in this loop we get all teams in our all leagues to a 'all_teams' list 
	for league in leagues:
		all_teams += league.team_set.all()

	#in this loop we get all new form every team which is in 'all_teams' list and place that new into 'all_news' list  
	for team in all_teams:
		all_news += team.news_set.all()

	#sort news by date so that last news pop up first
	all_news = reversed(sorted(all_news, key=lambda ne:ne.date))
	#taking forst 50 news of all news
	all_news = list(all_news)[:50]
	#context data initialization into dictionary 'args'
	args['news'] = all_news
	args['leagues'] = leagues

	return render_to_response('news/index.html',args)

def league(request,league_id=1):
	"""return rendered news page for particular league"""

	#define variables
	args = {}
	news = []

	#getting data form models
	this_league = get_object_or_404(League, pk = league_id)
	leagues = League.objects.all().exclude(pk = league_id).order_by('name')
	teams = this_league.team_set.all().order_by('name')
	
	#collecting all news of leagu into 'news' list
	for team in teams:
		news += team.news_set.all()

	#sort news by date so that last news pop up first
	news = reversed(sorted(news, key=lambda ne:ne.date))
	#taking forst 40 news of all news
	news = list(news)[:40]
	#context data initialization into dictionary 'args'
	args['teams'] = teams
	args['this_league'] = this_league
	args['leagues'] = leagues
	args['news'] = news

	return render_to_response('news/league.html',args)
	
def team(request,league_id = 1,team_id = -1):
	"""return rendered news page for particular team"""

	#define variables
	args = {}

	#getting data form models
	this_team = get_object_or_404(Team, pk = team_id)
	news = this_team.news_set.all().order_by('date')
	this_league = get_object_or_404(League, pk = league_id)
	teams = this_league.team_set.all().exclude(pk = team_id).order_by('name')
	leagues = League.objects.all().exclude(pk = league_id).order_by('name')

	#context data initialization into dictionary 'args'
	args['this_team'] = this_team
	args['this_league'] = this_league
	args['teams'] = teams
	args['leagues'] = leagues
	args['news'] = news
	
	return render_to_response('news/team.html',args)

def news(request,news_id):
	""" returns particular rendered news """

	#define variables
	args = {}
	
	#getting data form models
	news = get_object_or_404(News, pk = news_id)
	leagues = League.objects.all().order_by('name')

	#context data initialization into dictionary 'args'
	args['news'] = news
	args['leagues'] = leagues

	return render_to_response('news/news.html',args)
