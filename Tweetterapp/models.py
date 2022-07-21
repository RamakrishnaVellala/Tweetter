from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=140)
    image = models.ImageField(default='default.png', upload_to='profiles_pics')

    def __str__(self):
        return f"{self.user.username}"


class Tweet(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    content_image = models.ImageField(upload_to='tweets', blank=True)
    likers = models.ManyToManyField(User, blank=True, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content


class Comment(models.Model):
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenters')
    comment_content = models.TextField(max_length=90)
    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Tweet: {self.tweet} | Commenter: {self.commenter}"


class Follower(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ManyToManyField(
        User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.user}"
