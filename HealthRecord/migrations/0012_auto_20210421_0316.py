# Generated by Django 3.1.7 on 2021-04-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthRecord', '0011_userhealthdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhealthdata',
            name='blood_pressure',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='userhealthdata',
            name='bmi_index',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='userhealthdata',
            name='height',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='userhealthdata',
            name='weight',
            field=models.CharField(default='', max_length=120),
        ),
    ]
