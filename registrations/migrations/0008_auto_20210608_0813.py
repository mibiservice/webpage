# Generated by Django 3.2.1 on 2021-06-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0007_alter_workersform_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WorkersForm',
        ),
        migrations.AlterField(
            model_name='workers',
            name='categories',
            field=models.CharField(choices=[('Digital shop', 'Digital shop'), ('Other shop', 'Other shop'), ('Individual with no shop', 'Individual with no shop')], max_length=100),
        ),
    ]