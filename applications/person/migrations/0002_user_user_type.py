# Generated by Django 3.2.4 on 2021-07-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('0', 'Comprador'), ('1', 'Vendedor')], default='0', max_length=1),
        ),
    ]
