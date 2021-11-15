# Generated by Django 3.2.8 on 2021-11-13 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20211113_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussinessRegistration',
            fields=[
                ('BussinessID', models.AutoField(primary_key=True, serialize=False)),
                ('PropertyID', models.PositiveIntegerField(blank=True)),
                ('licenseNO', models.CharField(max_length=500)),
                ('BussinessName', models.CharField(max_length=500)),
                ('BussinessType', models.CharField(max_length=500)),
                ('BussinessGrade', models.CharField(max_length=500)),
                ('Type', models.CharField(max_length=500)),
                ('BillingType', models.CharField(max_length=500)),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.district')),
                ('Neighbor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.neighbor')),
                ('PlotNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.plotno')),
                ('SubDistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subdistrict')),
            ],
        ),
        migrations.CreateModel(
            name='BussinessStatus',
            fields=[
                ('BussinessID', models.AutoField(primary_key=True, serialize=False)),
                ('StatusType', models.CharField(max_length=500)),
                ('StatusDate', models.DateField()),
                ('BussinessReg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessregistration')),
            ],
        ),
        migrations.CreateModel(
            name='BussinessRegistrator',
            fields=[
                ('RegistrationID', models.AutoField(primary_key=True, serialize=False)),
                ('RegFirstName', models.CharField(max_length=500)),
                ('BussinessSecondName', models.CharField(max_length=500)),
                ('BussinessLastName', models.CharField(max_length=500)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('Telephone', models.CharField(max_length=500)),
                ('BussinessReg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessregistration')),
            ],
        ),
    ]
