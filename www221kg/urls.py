from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www221kg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^special/', include(admin.site.urls)),
    url(r'^reservation/',include('reservation.urls',namespace='reservation')),
    url(r'^news/',include('news.urls',namespace='news')),
    url(r'^bet/',include('bet.urls', namespace='bet')),
    url(r'^pro/',include('pro_owner.urls', namespace='pro_owner')),
	url(r'^',include('main.urls',namespace='main')),
    url(r'^',include('password_reset.urls')),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
urlpatterns += patterns('',
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT}))

