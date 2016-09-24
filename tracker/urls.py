from django.conf.urls import url


from tracker import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^task/$', views.TaskListView.as_view(), name='task-list'),
    url(r'^task/add_task/$', views.add_task, name='task-add'),
    # url(r'^task/$', views.add_task(), name='add_task'),
    # url(r'^add_task/$', views.add_task(), name='add_task'),
]
