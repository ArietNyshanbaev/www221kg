from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kgzone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'bet.views.index', name='index'),
    url(r'^make_bet$', 'bet.views.make_bet', name='make_bet'),
    url(r'^archive$', 'bet.views.archive', name='archive'),
    url(r'^best_betters$', 'bet.views.best_betters', name='best_betters'),
    url(r'^tour_result/more_info/(?P<betid>\d+)$', 'bet.views.more_info', name='more_info'),
    url(r'^tour_result/(?P<tourid>\d+)$', 'bet.views.tour_result', name='tour_result'),
    url(r'^check/(?P<tourid>\d+)$', 'bet.views.check', name='check'),
    url(r'^team$', 'bet.views.team', name='team'),
    url(r'^how_it_works$', 'bet.views.how_it_works', name='how_it_works'),

)