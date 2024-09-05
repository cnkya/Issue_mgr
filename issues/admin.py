from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "summary", "status", "description", "reporter", "created_on"

    ]

admin.site.register(Issue, IssueAdmin)
