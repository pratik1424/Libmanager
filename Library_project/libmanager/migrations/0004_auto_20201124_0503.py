# Generated by Django 3.1.3 on 2020-11-24 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libmanager', '0003_auto_20201124_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_detail',
            old_name='Gender',
            new_name='gender',
        ),
    ]
