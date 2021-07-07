from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField(max_length=200, blank=False)
    to_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='from_user')
    like = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now())
