from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    body = models.TextField()


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
