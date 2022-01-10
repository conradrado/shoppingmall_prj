from django.db import models
class Post(models.Model)
    title = models.Charfield(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField()
# Create your models here.
