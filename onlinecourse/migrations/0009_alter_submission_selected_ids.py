# Generated by Django 4.0.3 on 2022-04-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0008_alter_submission_selected_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='selected_ids',
            field=models.CharField(default='', max_length=50),
        ),
    ]
