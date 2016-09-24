from __future__ import division, print_function, unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __unicode__(self):
        return self.user.username


class Task(models.Model):

    STATUS_VALUES = Choices(
        (1, 'NOT_STARTED',  _('Not Started')),
        (2, 'IN_PROGRESS',  _('In Progress')),
        (3, 'COMPLETED',    _('Completed')),
    )

    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_VALUES,
        default=STATUS_VALUES.NOT_STARTED,
    )
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL,
                             related_name='tasks')

    def __unicode__(self):
        return self.name

#
# class Page(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(max_length=128)
#     url = models.URLField()
#     views = models.IntegerField(default=0)
#
#     def __str__(self):  # For Python 2, use __unicode__ too
#         return self.title