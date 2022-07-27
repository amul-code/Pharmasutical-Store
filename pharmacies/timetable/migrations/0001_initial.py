# Generated by Django 3.0.1 on 2020-01-27 10:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(blank=True,
                                         choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'),
                                                  (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=250)),
                ('slot4h', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1),
                                                                      django.core.validators.MaxValueValidator(6)])),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Pharmacy')),
            ],
            options={
                'verbose_name_plural': 'Timetables',
            },
        ),
    ]