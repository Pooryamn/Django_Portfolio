# Generated by Django 3.0.6 on 2020-05-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300)),
                ('Image', models.ImageField(upload_to='portfolio/images/')),
                ('Url', models.URLField(blank=True)),
            ],
        ),
    ]
