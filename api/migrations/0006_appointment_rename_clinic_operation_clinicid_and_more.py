# Generated by Django 4.0.2 on 2022-03-03 21:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_title_operation_title_rename_title_room_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 3, 23, 42, 26, 447431))),
                ('duration', models.IntegerField(default=0)),
                ('reason', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='clinic',
            new_name='clinicID',
        ),
        migrations.RenameField(
            model_name='paymentjournal',
            old_name='journal_entry_type',
            new_name='journal_entry_typeID',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='clinic',
            new_name='clinicID',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='clinic',
            new_name='clinicID',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='roleId',
            new_name='roleID',
        ),
        migrations.RenameField(
            model_name='visit',
            old_name='room',
            new_name='roomID',
        ),
        migrations.RenameField(
            model_name='visit_operation',
            old_name='operation',
            new_name='operationID',
        ),
        migrations.RenameField(
            model_name='visit_operation',
            old_name='visit',
            new_name='visitID',
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(default='doctor', max_length=100),
        ),
        migrations.DeleteModel(
            name='Appointmemt',
        ),
        migrations.AddField(
            model_name='appointment',
            name='createdbyID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to='api.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='api.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='roomID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.room'),
        ),
    ]