# Generated by Django 3.1.6 on 2021-02-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
