# Generated by Django 5.0.1 on 2024-02-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('phone_numer', models.CharField(max_length=10)),
            ],
        ),
    ]
