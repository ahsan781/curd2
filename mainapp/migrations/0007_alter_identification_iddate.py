# Generated by Django 3.2.8 on 2021-11-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_secondid_identification_scanedid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identification',
            name='IDdate',
            field=models.DateField(),
        ),
    ]