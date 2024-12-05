# Generated by Django 5.1.3 on 2024-12-04 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=100)),
                ('taskdescription', models.CharField(max_length=1000)),
                ('taskduedate', models.DateField()),
                ('taskstatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.taskstatus')),
            ],
        ),
    ]