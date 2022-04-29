# Generated by Django 4.0.4 on 2022-04-24 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_visit_operation_operation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit_operation',
            name='operation',
        ),
        migrations.AddField(
            model_name='visit_operation',
            name='operation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.operation'),
        ),
    ]