from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False, verbose_name='completed')

    def __unicode__(self):
        return self.title
