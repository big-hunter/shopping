# Generated by Django 3.0.6 on 2020-05-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_goods_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='discount',
            field=models.FloatField(default=1),
        ),
    ]
