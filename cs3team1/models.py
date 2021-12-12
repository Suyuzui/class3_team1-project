from django.db import models
from django.utils import timezone
from django.conf import settings




# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    context = models.TimeField("本文")
    created = models.DateTimeField("作成日",default=timezone.now)

    def __str__(self):
        return self.title