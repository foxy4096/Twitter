from django.db import models
from django.contrib.auth import get_user_model

class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(max_length=150)
    likes = models.ManyToManyField(get_user_model(), related_name='tweet_user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.body
