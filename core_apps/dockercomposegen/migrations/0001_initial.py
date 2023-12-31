# Generated by Django 4.2.7 on 2023-11-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DockerComposeInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
                ('value', models.TextField(verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Docker Compose Instruction',
                'verbose_name_plural': 'Docker Compose Instructions',
                'unique_together': {('key', 'value')},
            },
        ),
    ]
