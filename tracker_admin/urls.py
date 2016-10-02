from django.contrib import admin

from django.conf import settings
from django.conf.urls import include, url

from tracker.api.urls import api_v1_urlpatterns

from tracker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    if settings.COMBINE_API_AND_WEB_URLS:
        urlpatterns += [
            url(r'^api/1/', include(api_v1_urlpatterns, namespace='api')),
        ]