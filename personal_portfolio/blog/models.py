from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_created=True)
    text = models.TextField()

    def __str__(self):
        return self.title

