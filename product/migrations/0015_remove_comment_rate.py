# Generated by Django 3.0.4 on 2020-05-10 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
    ]