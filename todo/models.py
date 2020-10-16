from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=now)
    manager=models.ForeignKey(User, on_delete=models.PROTECT)

    def toggleStatus(self):
        self.done = not self.done
        self.save()

    def __str__(self):
        return self.title
