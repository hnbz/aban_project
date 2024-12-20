# Generated by Django 5.1.3 on 2024-11-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=255, unique=True)),
                ('price_buy', models.DecimalField(decimal_places=10, max_digits=20)),
                ('price_sell', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
