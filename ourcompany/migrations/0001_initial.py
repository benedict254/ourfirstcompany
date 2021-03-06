# Generated by Django 3.0.2 on 2020-03-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='past_pics')),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=16)),
                ('facilitator', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField()),
                ('venue', models.CharField(max_length=55)),
            ],
        ),
    ]
