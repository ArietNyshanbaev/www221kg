from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kgzone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'reservation.views.index', name='index'), 
    url(r'^schedule/(?P<field_id>\d+)$', 'reservation.views.schedule', name='schedule'),
    url(r'^reserve/(?P<field_id>\d+)/(?P<day_id>\d+)$', 'reservation.views.reserve', name='reserve'),
    url(r'^list$', 'reservation.views.list', name='list'),
    url(r'^team$', 'reservation.views.team', name='team'),
)

