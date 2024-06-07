# Generated by Django 5.0.4 on 2024-04-25 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unwanted_teammates', models.ManyToManyField(blank=True, to='teams.player')),
            ],
        ),
        migrations.CreateModel(
            name='HCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2024)),
                ('hcp', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2024)),
                ('show', models.BooleanField(default=False)),
                ('players', models.ManyToManyField(to='teams.player')),
            ],
        ),
    ]
