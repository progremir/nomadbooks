from django.db import models

from common.models import TimestampModel


class Category(TimestampModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
