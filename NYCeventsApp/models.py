# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Places(models.Model):
    id = models.IntegerField(primary_key=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    borough = models.CharField(max_length=30, blank=True, null=True)
    zone = models.CharField(max_length=30, blank=True, null=True)
    service_zone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'

    def __str__(self):
        return '%s %s %s' % (self.id, self.borough, self.zone)


class Taxistrips(models.Model):
    vendorid = models.IntegerField(blank=True, null=True)
    tpep_pickup_datetime = models.DateTimeField(blank=True, null=True)
    tpep_dropoff_datetime = models.DateTimeField(blank=True, null=True)
    passenger_count = models.IntegerField(blank=True, null=True)
    trip_distance = models.IntegerField(blank=True, null=True)
    ratecodeid = models.IntegerField(blank=True, null=True)
    store_and_fwd_flag = models.CharField(max_length=10, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    fare_amount = models.IntegerField(blank=True, null=True)
    extra = models.IntegerField(blank=True, null=True)
    mta_tax = models.IntegerField(blank=True, null=True)
    improvement_surcharge = models.IntegerField(blank=True, null=True)
    tip_amount = models.IntegerField(blank=True, null=True)
    tolls_amount = models.IntegerField(blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    pulocationid = models.ForeignKey(Places, models.DO_NOTHING, db_column='pulocationid', blank=True, null=True, related_name='pul')
    dolocationid = models.ForeignKey(Places, models.DO_NOTHING, db_column='dolocationid', blank=True, null=True, related_name='dol')

    class Meta:
        managed = False
        db_table = 'taxistrips'

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.trip_distance, self.pulocationid.borough, self.dolocationid.borough)