from django.db import models

# Create your models here.

class FeedItem(models.Model):
    title = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null=True)
    domain = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(null=False)
    source_date = models.DateTimeField(null=True)
    photo_link = models.CharField(max_length=200, null=True)
    byline = models.CharField(max_length=200, null=True)
    excerpt = models.CharField(max_length=200, null=False)