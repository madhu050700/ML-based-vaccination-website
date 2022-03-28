# Generated by Django 3.1.6 on 2021-02-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20210224_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupform',
            old_name='Name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='signupform',
            name='bloodgroup',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signupform',
            name='locationinfo',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signupform',
            name='mobileno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signupform',
            name='pname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='signupform',
            table='patients_info',
        ),
    ]
