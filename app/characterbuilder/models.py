from django.db import models


class Character(models.Model):
    """Contains information of a story character"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name