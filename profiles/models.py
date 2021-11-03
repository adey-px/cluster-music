from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# When user signup, create one profile for each user using - OneToOneField
class UserProfile(models.Model):
    """ A user profile model for capturing summary of user activity
    on_delete=models keeps user activity in db, even after deleting the user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # At login, return user's username on designated page -eg- profile.html
    def __str__(self):
        return self.user.username


# Attach quick receiver for post-save events from user model above
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Each time user object is saved, automatically create or update user profile
    if already existed. All users created b4 creating the UserProfile model
    won't be able to login again. Comment out d lines below to allow them login.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
