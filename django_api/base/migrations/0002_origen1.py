# Generated by Django 5.0.3 on 2024-03-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origen1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surnames', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
