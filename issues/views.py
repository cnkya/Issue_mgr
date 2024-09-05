from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    
)
from .models import Issue, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    
)

class IssueListView(LoginRequiredMixin, ListView):    #scan operation
    template_name = "issues/list.html"
    model = Issue

    

class IssueDetailView(LoginRequiredMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue

    def test_func(self):
        post = self.get_object()
        return issue.reporter == self.request.user

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "status", "description", "reporter"  ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "issues/update.html"
    model = Issue
    fields = ["summary", "status", "priority", "description", "reporter", "user" ]

    def test_func(self):
        post = self.get_object()
        return issue.reporter == self.request.user
    