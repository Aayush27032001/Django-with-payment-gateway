# Generated by Django 3.0.5 on 2021-05-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]
