from __future__ import division, print_function, unicode_literals

import vanilla

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

from tracker.models import Task
from tracker.forms import TaskForm


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'index.html', context=context_dict)


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('task-list'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


class TaskMixin(object):
    """
    Add user to the context
    """
    def get_context_data(self, *args, **kwargs):
        context = super(TaskMixin, self).get_context_data(*args, **kwargs)

        if hasattr(self, "request") and self.request.user and self.request.user.is_authenticated():
            context.update({
                'username': self.request.user.username,
            })
        return context

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login'))
        else:
            return super(TaskMixin, self).dispatch(request, *args, **kwargs)


class TaskListView(TaskMixin, vanilla.ListView):
    model = Task
    template_name = 'tracker/task/list_task.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context.update({
            'tasks': self.get_queryset(),
        })
        return context

    def get_queryset(self):
        qs = super(TaskListView, self).get_queryset()
        # only get the Tasks associated with this user
        qs = qs.filter(user=self.request.user)
        qs = qs.order_by('order')
        return qs


class TaskCreateView(TaskMixin, vanilla.CreateView):
    model = Task
    template_name = 'tracker/task/add_task.html'
    form_class = TaskForm
    success_url = "/tracker/task/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(*args, **kwargs)
        return context


class TaskUpdateView(TaskMixin, vanilla.UpdateView):
    model = Task
    template_name = 'tracker/task/update.html'
    form_class = TaskForm
    success_url = "/tracker/task/"

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)
        return context


class TaskDeleteView(TaskMixin, vanilla.DeleteView):
    model = Task
    template_name = 'tracker/task/delete.html'
    form_class = TaskForm
    success_url = "/tracker/task/"

    def get_context_data(self, *args, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(*args, **kwargs)
        return context


@login_required
def complete_task(request):

    task_id = None
    if request.method == 'GET':
        task_id = request.GET['task_id']
    if task_id:
        task = Task.objects.get(id=int(task_id))
        if task:
            task.status = Task.STATUS_VALUES.COMPLETED
            task.save()
    return HttpResponse(task.get_status_display())
