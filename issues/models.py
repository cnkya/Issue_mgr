from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Issue(models.Model):
    summary = models.CharField(max_length=256)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name



