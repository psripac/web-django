from django.db import models
from datetime import datetime

# Create your models here.
class Sample(models.Model):
    sample_title = models.CharField(max_length=200)
    sample_content = models.TextField()
    sample_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.sample_title