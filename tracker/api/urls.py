from __future__ import division, print_function, unicode_literals

import os

from django.conf import settings
# from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, UserProfileViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)

# from .views.base import ping

# Break this out so djed.urls can use it and root it apart from us.
api_v1_urlpatterns = [
    url(r'^', include(router.urls)),

    # url(r'^users/$',
    #     UserViewSet.as_view(),
    #     name='users'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # url(r'',
    #     include('djed.api.assets.urls', namespace='assets')),
    #
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #
    # url(r'^ping/$', ping, name='ping')
]

urlpatterns = [
    url(r'^api/1/', include(api_v1_urlpatterns, namespace='api')),
]

# if settings.DEBUG and settings.HAS_DEBUG_TOOLBAR and not os.environ.get(
#         'DISABLE_DEBUG_TOOLBAR', False):
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
