# Generated by Django 2.0.7 on 2018-09-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180901_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
