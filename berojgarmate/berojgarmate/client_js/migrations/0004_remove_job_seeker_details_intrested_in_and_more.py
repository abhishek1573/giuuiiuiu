# Generated by Django 4.2.1 on 2023-10-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_js', '0003_rename_intested_in_job_seeker_details_intrested_in_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_seeker_details',
            name='intrested_in',
        ),
        migrations.AlterField(
            model_name='job_seeker_details',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterModelTable(
            name='job_seeker_details',
            table=None,
        ),
    ]
