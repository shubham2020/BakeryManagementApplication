# Generated by Django 3.1.6 on 2021-02-16 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profit', models.FloatField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount', to='bakery.ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='EndProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('bakeryItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount', to='bakery.bakeryitems')),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('bakeryItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.bakeryitems')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.ingredients')),
            ],
        ),
    ]
