from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appname.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'news.views.index', name='index'),
    url(r'^team/(?P<league_id>\d+)/(?P<team_id>\d+)$', 'news.views.team', name='team'),
    url(r'^league/(?P<league_id>\d+)$', 'news.views.league', name='league'),
    url(r'^news/(?P<news_id>\d+)$', 'news.views.news', name='news'),
)