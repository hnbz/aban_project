# Generated by Django 5.1.3 on 2024-11-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_deposit_amount_alter_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='after_balance',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='before_balance',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
