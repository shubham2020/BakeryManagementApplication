# Generated by Django 3.1.6 on 2021-02-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('symbol', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bakeryitems',
            name='ingredients',
            field=models.ManyToManyField(through='bakery.Composition', to='bakery.Ingredients'),
        ),
        migrations.AlterField(
            model_name='bakeryitems',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='composition',
            unique_together={('bakeryItem', 'ingredients')},
        ),
        migrations.AddField(
            model_name='composition',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery.units'),
        ),
        migrations.AddField(
            model_name='endproducts',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery.units'),
        ),
        migrations.AddField(
            model_name='rawmaterials',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery.units'),
        ),
    ]