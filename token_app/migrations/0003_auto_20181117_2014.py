# Generated by Django 2.1.3 on 2018-11-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0002_auto_20181117_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testapp',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
