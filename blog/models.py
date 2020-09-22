from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now changes datetime everytime the entry is modified
    # auto_now_add - changes when entry is created
    date_posted = models.DateTimeField(default=timezone.now)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Instead of below code, we can set success_url in PostCreateView to specify the redirect url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
