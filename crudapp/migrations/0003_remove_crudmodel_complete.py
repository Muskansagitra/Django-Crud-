# Generated by Django 5.0.7 on 2024-07-14 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_crudmodel_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crudmodel',
            name='complete',
        ),
    ]
