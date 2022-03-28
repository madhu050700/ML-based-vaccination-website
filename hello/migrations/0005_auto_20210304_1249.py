# Generated by Django 3.1.6 on 2021-03-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20210224_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=25)),
                ('bloodgroup', models.CharField(max_length=25)),
                ('locationinfo', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=3)),
                ('ailments', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.DeleteModel(
            name='SignupForm',
        ),
    ]
