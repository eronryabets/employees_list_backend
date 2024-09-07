# Generated by Django 5.1.1 on 2024-09-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('years_worked', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
