# Generated by Django 2.1.7 on 2019-04-12 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderAPI', '0008_auto_20190411_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordcloud', models.TextField(blank=True, verbose_name='微博词云')),
                ('UserInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderAPI.UserInfo', verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '微博词云',
                'verbose_name_plural': '微博词云',
            },
        ),
        migrations.RemoveField(
            model_name='sentimentsinfo',
            name='UserInfo',
        ),
        migrations.AlterField(
            model_name='tweetsinfo',
            name='pinyin',
            field=models.TextField(blank=True, verbose_name='词性'),
        ),
        migrations.DeleteModel(
            name='SentimentsInfo',
        ),
    ]