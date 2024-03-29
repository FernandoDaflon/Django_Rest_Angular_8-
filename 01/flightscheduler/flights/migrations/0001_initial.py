# Generated by Django 3.0 on 2019-12-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=200)),
                ('flight_no', models.CharField(max_length=10)),
                ('trip_type', models.CharField(max_length=50)),
                ('departure_airport', models.CharField(max_length=10)),
                ('arrival_airport', models.CharField(max_length=10)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
            ],
        ),
    ]
