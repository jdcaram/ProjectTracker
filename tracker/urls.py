from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url

from api.urls import api_v1_urlpatterns
from tracker import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^task/$', views.TaskListView.as_view(), name='task-list'),
    url(r'^task/add_task/$', views.TaskCreateView.as_view(), name='task-add'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.TaskUpdateView.as_view(), name='task-update'),
    url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name='task-delete'),

    url(r'^task/complete/$', views.complete_task, name='task-complete'),
    # url(r'^task/$', views.add_task(), name='add_task'),
    # url(r'^add_task/$', views.add_task(), name='add_task'),
]


