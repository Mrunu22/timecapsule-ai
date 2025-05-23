from django.db import models
from django.contrib.auth.models import User

class Capsule(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    unlock_date = models.DateTimeField()

    def __str__(self):
        return self.title
