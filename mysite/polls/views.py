from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import TaskToDo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TaskToDoList(LoginRequiredMixin, ListView):
    model = TaskToDo
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskToDoListDetail(LoginRequiredMixin, DetailView):
    model = TaskToDo
    context_object_name = 'tasks'


class TaskToDoListCreate(LoginRequiredMixin, CreateView):
    model = TaskToDo
    fields = ['title', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'polls/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskToDoListCreate, self).form_valid(form)


class TaskToDoListUpdate(LoginRequiredMixin, UpdateView):
    model = TaskToDo
    fields = ['title', 'complete']
    success_url = reverse_lazy('tasks')


class TaskToDoListDelete(LoginRequiredMixin, DeleteView):
    model = TaskToDo
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')


class Login(LoginView):
    fields = '__all__'
    redirect_authenticated_user = False
    template_name = 'polls/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks')


class Registration(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registration, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registration, self).get(*args, *kwargs)
    template_name = 'polls/register.html'
