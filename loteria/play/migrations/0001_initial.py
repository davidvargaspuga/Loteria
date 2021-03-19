# Generated by Django 3.1.7 on 2021-03-19 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_col', models.CharField(max_length=3)),
                ('second_col', models.CharField(max_length=3)),
                ('third_col', models.CharField(max_length=3)),
                ('fourth_col', models.CharField(max_length=3)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='play.card')),
            ],
        ),
    ]
