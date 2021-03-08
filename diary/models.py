from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Entry(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
