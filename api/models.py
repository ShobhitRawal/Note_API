from django.db import models
from django.http import JsonResponse

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField()

def __str__(self):
    return '%s %s' % (self.title, self.body)

