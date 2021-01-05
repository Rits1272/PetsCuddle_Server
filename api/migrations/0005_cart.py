# Generated by Django 3.1.4 on 2021-01-05 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
