# Generated by Django 3.1.7 on 2021-03-19 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='row',
            old_name='first_col',
            new_name='first_val',
        ),
        migrations.RenameField(
            model_name='row',
            old_name='fourth_col',
            new_name='fourth_val',
        ),
        migrations.RenameField(
            model_name='row',
            old_name='second_col',
            new_name='second_val',
        ),
        migrations.RenameField(
            model_name='row',
            old_name='third_col',
            new_name='third_val',
        ),
    ]