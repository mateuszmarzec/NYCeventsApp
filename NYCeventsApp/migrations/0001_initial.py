# Generated by Django 2.0 on 2017-12-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('borough', models.CharField(blank=True, max_length=30, null=True)),
                ('zone', models.CharField(blank=True, max_length=30, null=True)),
                ('service_zone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'places',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taxistrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorid', models.IntegerField(blank=True, null=True)),
                ('tpep_pickup_datetime', models.DateTimeField(blank=True, null=True)),
                ('tpep_dropoff_datetime', models.DateTimeField(blank=True, null=True)),
                ('passenger_count', models.IntegerField(blank=True, null=True)),
                ('trip_distance', models.IntegerField(blank=True, null=True)),
                ('ratecodeid', models.IntegerField(blank=True, null=True)),
                ('store_and_fwd_flag', models.CharField(blank=True, max_length=10, null=True)),
                ('payment_type', models.IntegerField(blank=True, null=True)),
                ('fare_amount', models.IntegerField(blank=True, null=True)),
                ('extra', models.IntegerField(blank=True, null=True)),
                ('mta_tax', models.IntegerField(blank=True, null=True)),
                ('improvement_surcharge', models.IntegerField(blank=True, null=True)),
                ('tip_amount', models.IntegerField(blank=True, null=True)),
                ('tolls_amount', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'taxistrips',
                'managed': False,
            },
        ),
    ]
