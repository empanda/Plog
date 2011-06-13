from django.db import models

from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    html = models.TextField()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.title
