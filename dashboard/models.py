from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)
    resolution = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.name

class ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    resolved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='resolved_tickets')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    resolution = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
