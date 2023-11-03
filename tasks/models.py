from django.db import models
from django.contrib.auth.models import User

STATUS_TYPES = (
    ("TO_DO", 'To Do'),
    ("IN_PROGRESS", 'In Progress'),
    ("DONE", 'Done'),
)


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_TYPES)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def as_json(self):
        return dict(
            id=self.pk,
            title=self.title,
            status=self.status,
            description=self.description,
            due_date=self.due_date.strftime('%Y-%m-%d')
        )

    class Meta:
        db_table = 't_tasks'
