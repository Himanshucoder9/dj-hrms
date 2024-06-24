from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(verbose_name="created date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated date", auto_now=True)

    class Meta:
        verbose_name = 'TimeStamp'
        verbose_name_plural = 'TimeStamps'
        abstract = True