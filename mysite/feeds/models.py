from django.db import models

# Create your models here.

class FeedItem(models.Model):
    title = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(null=False)