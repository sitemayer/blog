from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 128)
    date = models.DateTimeField(auto_now_add = True)
    summary = models.TextField(blank = True, null = True)
    content = models.TextField(blank = True, null = True)
    views = models.IntegerField()
    hearts = models.IntegerField()
    index = models.IntegerField(default = 0, primary_key=True)

    def page(self):
        return self.index / 2

    def __unicode__(self):
        return self.title
