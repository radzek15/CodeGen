# Generated by Django 4.2.7 on 2023-11-14 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dockerfilegen', '0002_alter_dockercommand_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dockercommand',
            options={'ordering': ['instruction'], 'verbose_name': 'Docker Command', 'verbose_name_plural': 'Docker Commands'},
        ),
    ]
