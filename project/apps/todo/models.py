from django.db import models


class TodoItem(models.Model):
    label = models.CharField(max_length=50)
    completed = models.BooleanField(default=False, verbose_name='completed')

    def __unicode__(self):
        return self.label
