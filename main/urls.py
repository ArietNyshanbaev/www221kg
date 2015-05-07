from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kgzone.views.home', name='home'),    reset_password_complate
    # url(r'^blog/', include('blog.urls')),     

    url(r'^$', 'main.views.main', name='main'),
    url(r'^signin/(?P<key>.+)$', 'main.views.signin', name='signin'),
    url(r'^signin$', 'main.views.signin', name='signin'),
    url(r'^signup$', 'main.views.signup', name='signup'),
    url(r'^signout$', 'main.views.signout', name='signout'),
    url(r'^team$', 'main.views.team', name='team'),
    url(r'^profile/modify_profile/$', 'main.views.modify_profile', name='modify_profile'),
    url(r'^profile/change_password/$', 'main.views.change_password', name='change_password'),
    url(r'^profile/$', 'main.views.profile', name='profile'),
)