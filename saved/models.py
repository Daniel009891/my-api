from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Saved(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='saved', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    