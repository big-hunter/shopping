# Generated by Django 3.0.6 on 2020-05-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200524_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='last_time_buy',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='login_out',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
