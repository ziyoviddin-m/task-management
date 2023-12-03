from django.db import models


class TaskCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    attachments = models.FileField(upload_to='task_attachments', blank=True, null=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

