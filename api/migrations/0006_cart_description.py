# Generated by Django 3.1.4 on 2021-01-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
