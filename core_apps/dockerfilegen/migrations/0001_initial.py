# Generated by Django 4.2.7 on 2023-11-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DockerCommand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(verbose_name='command instruction')),
                ('argument', models.CharField(blank=True, verbose_name='command argument')),
                ('variable', models.TextField(blank=True, verbose_name='command variable')),
            ],
            options={
                'verbose_name': 'Command',
                'verbose_name_plural': 'Commands',
                'ordering': ['instruction'],
            },
        ),
    ]
