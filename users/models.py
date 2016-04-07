from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, class_prepared



class Profile(models.Model):
    owner = models.OneToOneField('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=100000,default='')


    def __unicode__(self):
        return unicode(self.owner)

    def __str__(self):
        return str(self.owner)


def create_user_Info(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(owner=instance)

post_save.connect(create_user_Info, sender=User)


