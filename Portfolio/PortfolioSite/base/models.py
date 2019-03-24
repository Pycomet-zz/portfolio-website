from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


class Contact(models.Model):
    """Portfolio model"""
    
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=10000)
    
    def __str__(self):
        return 'Contact Me!'

    def create_user_profile(sender, instance, created, **kwargs):
        """Creates a profile for each registered regular user"""

        if created and instance:
            Contact.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def save(self, *args, **kwargs):
        """Save profile and resize profile image"""

        super(Contact, self).save(*args, **kwargs)