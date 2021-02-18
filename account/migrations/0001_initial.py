# Generated by Django 3.1.6 on 2021-02-16 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('placed', 'Placed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bakery.bakeryitems')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.orders')),
            ],
        ),
    ]