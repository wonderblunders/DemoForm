# Generated by Django 4.1.5 on 2023-01-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prune', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='country',
            field=models.CharField(choices=[('1', 'INDIA'), ('2', 'USA')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='currency_rx',
            field=models.CharField(choices=[('1', 'INR'), ('2', 'USD')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='currency_tx',
            field=models.CharField(choices=[('1', 'INR'), ('2', 'USD')], default='1', max_length=1),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
