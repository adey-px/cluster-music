from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Audio(models.Model):
    """ A model that adds Audio music songs to db """

    title = models.CharField(max_length=20, blank=False, null=False)
    artist = models.CharField(max_length=20, blank=False, null=False)
    song = models.FileField(blank=False, null=False)
    label = models.ImageField('Photo')
    link = models.CharField(max_length=250, blank=True, null=True)
    duration = models.CharField(max_length=30)

    def __str__(self):
        return self.title