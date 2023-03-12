from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_Length=60)
    question = model.models.TextField(max_Length=400)
    priority = model.models.CharField( max_length=1, choice=)