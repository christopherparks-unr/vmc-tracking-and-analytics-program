# Generated by Django 3.1.2 on 2021-02-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportpresets',
            name='line_color',
        ),
        migrations.AddField(
            model_name='reportpresets',
            name='display_options',
            field=models.CharField(choices=[('Dots', 'Dots'), ('Lines', 'Lines'), ('Dots and Lines', 'Dots and Lines')], max_length=50, null=True),
        ),
    ]
