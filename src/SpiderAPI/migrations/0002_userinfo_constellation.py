# Generated by Django 2.1.7 on 2019-03-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='Constellation',
            field=models.CharField(blank=True, max_length=30, verbose_name='星座'),
        ),
    ]