# Generated by Django 4.2.3 on 2023-07-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='products',
        ),
    ]
