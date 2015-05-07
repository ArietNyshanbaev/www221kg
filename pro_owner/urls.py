from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kgzone.views.home', name='home'),    reset_password_complate
    # url(r'^blog/', include('blog.urls')),     

    url(r'^$', 'pro_owner.views.signin_as_owner', name='signin_as_owner'),
    url(r'^home$', 'pro_owner.views.home', name='home'),
    url(r'^info_field/(?P<field_id>\d+)$', 'pro_owner.views.info_field', name='info_field'),
    url(r'^info_day/(?P<field_id>\d+)/(?P<day_id>\d+)$', 'pro_owner.views.info_day', name='info_day'),
)