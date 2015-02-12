from {{cookiecutter.repo_name}}.models import DjangoDateModel
from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals


class UserProfile(DjangoDateModel):
    user = models.OneToOneField(
        User, related_name='profile')
    profile_picture = models.URLField(
        max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    def __unicode__(self):
        return u'{username}'.format(username=self.user.username)


def user_saved(sender, **kwargs):
    user = kwargs['instance']
    if not hasattr(user, 'profile'):
        from .models import UserProfile
        user.profile = UserProfile()
        user.profile.save()
        user.save()

signals.post_save.connect(user_saved, sender=User)
