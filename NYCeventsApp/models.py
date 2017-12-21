from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    additional = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'

    def __str__(self):
        return '%s %s %s' % (self.name, self.address, self.date)