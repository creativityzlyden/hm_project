# Generated by Django 3.0.6 on 2020-05-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0002_auto_20200515_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='gender',
            field=models.CharField(choices=[('not specified', 'not specified'), ('male', 'male'), ('female', 'female')], max_length=13),
        ),
    ]
