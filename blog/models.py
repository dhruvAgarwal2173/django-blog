from django.db import models
from django.conf import settings
from django.utils import timezone
import tinymce.models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=180, null=False)
    text = tinymce.models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def last_modified(self):
        self.last_modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title, self.author
