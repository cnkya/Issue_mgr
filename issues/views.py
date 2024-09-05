from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    
)
from .models import Issue, Status
from django.urls import reverse_lazy

class IssueListView(ListView):    #scan operation
    template_name = "issues/list.html"
    model = Issue

class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue

class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "status", "description", "reporter"  ]

class IssueUpdateView(UpdateView):
    template_name = "issues/update.html"
    model = Issue
    fields = ["summary", "status", "priority", "description", "reporter", "user" ]
    