from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """Base Model for all models"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(models.Model):
    """Every item in Saga application belongs to a project"""
    title = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.title