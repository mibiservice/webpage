# Generated by Django 3.2.1 on 2021-06-08 02:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0008_auto_20210608_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Digital shop', 'Digital shop'), ('Other shop', 'Other shop'), ('Individual with no shop', 'Individual with no shop')], max_length=100),
        ),
    ]
