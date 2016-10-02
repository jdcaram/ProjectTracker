from __future__ import division, print_function, unicode_literals

from django.contrib.auth.models import Group
from rest_framework import serializers

from tracker.models import UserProfile, User, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'website', 'picture')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'order',
            'status',
            # 'user',
        ]

