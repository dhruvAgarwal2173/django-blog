from django.db import models
from django.conf import settings
from django.utils import timezone
import tinymce.models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=180, null=False)
    text = tinymce.models.HTMLField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title, self.author
