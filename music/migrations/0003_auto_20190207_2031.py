# Generated by Django 2.1.4 on 2019-02-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190207_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='华语歌手',
            name='歌手姓名',
            field=models.CharField(max_length=500),
        ),
    ]
