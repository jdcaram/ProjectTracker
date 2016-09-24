from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from tracker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', admin.site.urls),
]
