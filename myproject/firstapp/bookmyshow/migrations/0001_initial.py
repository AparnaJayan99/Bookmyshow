# Generated by Django 4.1.5 on 2023-01-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('t_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(max_length=20)),
                ('showtime', models.CharField(max_length=50)),
            ],
        ),
    ]
