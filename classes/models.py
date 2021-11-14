from django.db import models

# Create your models here.


class Class(models.Model):
    """ Model for Classes"""

    class Meta:
        verbose_name_plural = 'Classes'

    class_name = models.CharField(max_length=32)
    class_time = models.CharField(max_length=32)
    class_type = models.CharField(max_length=32, null=True, blank=True)
    class_level = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.class_name

