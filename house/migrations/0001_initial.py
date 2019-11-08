# Generated by Django 2.2.5 on 2019-11-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(default='#')),
                ('address', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('categories', models.CharField(default='', max_length=200)),
                ('summary', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LonLatField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]
