# Generated by Django 3.1.6 on 2021-02-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=30)),
                ('images', models.FileField(upload_to='static/uploads/', verbose_name='images')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('options', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=150)),
            ],
        ),
    ]