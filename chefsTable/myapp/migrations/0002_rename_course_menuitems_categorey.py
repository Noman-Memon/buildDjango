# Generated by Django 4.1.4 on 2023-01-04 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='course',
            new_name='categorey',
        ),
    ]