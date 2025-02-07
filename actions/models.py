from django.db import models

class Action(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_last_done = models.DateTimeField(blank=True, null=True)
    date_last_not_done = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name