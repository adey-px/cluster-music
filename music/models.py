from django.db import models
from django.core.exceptions import ValidationError

from profiles.models import UserProfile


# Create your models here.


# Model for adding or uploading audio to db, note attached UserProfile
class Audio(models.Model):
    """ A model that adds Audio music songs to db. UserProfile model from
    profile app, is applied as ForeignKey and as done in that model,
    on_delete=models keeps user activity in db, even after deleting the user
    """

    title = models.CharField(max_length=20, blank=False, null=False)
    artist = models.CharField(max_length=20, blank=False, null=False)
    song = models.FileField(blank=False, null=False)
    label = models.ImageField('Photo')
    duration = models.CharField(max_length=30)
    published_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='audios')

    def __str__(self):
        return self.title
