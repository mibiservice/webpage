# Generated by Django 3.2.1 on 2021-06-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_alter_workers_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
