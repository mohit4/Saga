from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Project


class ProjectCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new project
    """
    template_name = "projectmanager/project_form.html"
    model = Project
    fields = ('title',)
    success_message = 'Created new project!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Create new Project"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating an existing project
    """
    template_name = "projectmanager/project_form.html"
    model = Project
    fields = ('title',)
    success_message = 'Project updated!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Update Project"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(ListView):
    """
    Listing all the projects present in database
    """
    template_name = "projectmanager/project_list.html"
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Listing all project(s)"
        return context


class ProjectDetailView(DetailView):
    """
    Printing details of a single project
    """
    template_name = "projectmanager/project_detail.html"
    model = Project
    context_object_name = "project"


class ProjectDeleteView(DeleteView):
    """
    Deleting an existing project
    """
    template_name = "projectmanager/project_detail.html"
    model = Project
    context_object_name = "project"
    success_url = reverse_lazy("projectmanager:project-list")
    success_message = 'Project deleted!'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)