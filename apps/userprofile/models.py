from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, default="default.jpg")
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def follow_user(self, to_follow):
        if to_follow != self:
            if to_follow in self.follows.all():
                self.follows.add(to_follow)
                return True
            else:
                self.follows.remove(to_follow)
                return False
        return False


    def __str__(self):
        return self.user.username
