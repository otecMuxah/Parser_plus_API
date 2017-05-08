from django.db import models

# Create your models here.


class NewsEntry(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    site = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.author, self.url, self.site)
