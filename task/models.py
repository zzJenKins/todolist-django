from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=255)
    status = models.IntegerField(choices=((0,'未开始'),(1,'已完成')))
    created = models.DateTimeField(default=datetime.utcnow)

