# Generated by Django 4.0.2 on 2022-04-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='roleID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.role'),
        ),
    ]
