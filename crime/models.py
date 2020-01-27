from django.db import models

class Crime(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=2100, default='url')
    description = models.TextField()