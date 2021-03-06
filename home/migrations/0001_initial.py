# Generated by Django 2.2.1 on 2019-09-29 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('leader_no', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('proj_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('grp', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('domain', models.CharField(max_length=50)),
                ('thrust_area', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('T_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('T_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
            ],
        ),
    ]
