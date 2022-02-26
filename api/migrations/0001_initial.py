# Generated by Django 4.0 on 2021-12-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.TextField()),
                ('word', models.TextField()),
                ('condition', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('F7_THETA', models.TextField()),
                ('F7_ALPHA', models.TextField()),
                ('F7_LOW_BETA', models.TextField()),
                ('F7_HIGH_BETA', models.TextField()),
                ('F7_GAMMA', models.TextField()),
                ('F3_THETA', models.TextField()),
                ('F3_ALPHA', models.TextField()),
                ('F3_LOW_BETA', models.TextField()),
                ('F3_HIGH_BETA', models.TextField()),
                ('F3_GAMMA', models.TextField()),
                ('AF3_THETA', models.TextField()),
                ('AF3_ALPHA', models.TextField()),
                ('AF3_LOW_BETA', models.TextField()),
                ('AF3_HIGH_BETA', models.TextField()),
                ('AF3_GAMMA', models.TextField()),
                ('FC5_THETA', models.TextField()),
                ('FC5_ALPHA', models.TextField()),
                ('FC5_LOW_BETA', models.TextField()),
                ('FC5_HIGH_BETA', models.TextField()),
                ('FC5_GAMMA', models.TextField()),
                ('T7_THETA', models.TextField()),
                ('T7_ALPHA', models.TextField()),
                ('T7_LOW_BETA', models.TextField()),
                ('T7_HIGH_BETA', models.TextField()),
                ('T7_GAMMA', models.TextField()),
                ('P7_THETA', models.TextField()),
                ('P7_ALPHA', models.TextField()),
                ('P7_LOW_BETA', models.TextField()),
                ('P7_HIGH_BETA', models.TextField()),
                ('P7_GAMMA', models.TextField()),
                ('O1_THETA', models.TextField()),
                ('O1_ALPHA', models.TextField()),
                ('O1_LOW_BETA', models.TextField()),
                ('O1_HIGH_BETA', models.TextField()),
                ('O1_GAMMA', models.TextField()),
                ('O2_THETA', models.TextField()),
                ('O2_ALPHA', models.TextField()),
                ('O2_LOW_BETA', models.TextField()),
                ('O2_HIGH_BETA', models.TextField()),
                ('O2_GAMMA', models.TextField()),
                ('P8_THETA', models.TextField()),
                ('P8_ALPHA', models.TextField()),
                ('P8_LOW_BETA', models.TextField()),
                ('P8_HIGH_BETA', models.TextField()),
                ('P8_GAMMA', models.TextField()),
                ('T8_THETA', models.TextField()),
                ('T8_ALPHA', models.TextField()),
                ('T8_LOW_BETA', models.TextField()),
                ('T8_HIGH_BETA', models.TextField()),
                ('T8_GAMMA', models.TextField()),
                ('FC6_THETA', models.TextField()),
                ('FC6_ALPHA', models.TextField()),
                ('FC6_LOW_BETA', models.TextField()),
                ('FC6_HIGH_BETA', models.TextField()),
                ('FC6_GAMMA', models.TextField()),
                ('F4_THETA', models.TextField()),
                ('F4_ALPHA', models.TextField()),
                ('F4_LOW_BETA', models.TextField()),
                ('F4_HIGH_BETA', models.TextField()),
                ('F4_GAMMA', models.TextField()),
                ('F8_THETA', models.TextField()),
                ('F8_ALPHA', models.TextField()),
                ('F8_LOW_BETA', models.TextField()),
                ('F8_HIGH_BETA', models.TextField()),
                ('F8_GAMMA', models.TextField()),
                ('AF4_THETA', models.TextField()),
                ('AF4_ALPHA', models.TextField()),
                ('AF4_LOW_BETA', models.TextField()),
                ('AF4_HIGH_BETA', models.TextField()),
                ('AF4_GAMMA', models.TextField()),
            ],
        ),
    ]
