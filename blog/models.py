from datetime import datetime

from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default= datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
