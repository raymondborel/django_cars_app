from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']