# Generated by Django 3.2.8 on 2021-11-13 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_propertyrevenu_parcel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussinessRevenu',
            fields=[
                ('BussinessID', models.AutoField(primary_key=True, serialize=False)),
                ('TransNo', models.PositiveIntegerField(blank=True)),
                ('TaransDate', models.DateField()),
                ('Chargecode', models.CharField(max_length=500)),
                ('Transcurr', models.CharField(max_length=500)),
                ('GrNo', models.CharField(max_length=500)),
                ('Revenuetype', models.CharField(max_length=500)),
                ('BussinessRevenu', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessregistration')),
            ],
        ),
    ]
