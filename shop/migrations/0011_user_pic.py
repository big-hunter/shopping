# Generated by Django 3.0.6 on 2020-05-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_address_order_orderinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.CharField(default='/static/images/header/default.jpg', max_length=100),
        ),
    ]