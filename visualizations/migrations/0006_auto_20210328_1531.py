# Generated by Django 3.1.2 on 2021-03-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0005_auto_20210327_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportpresets',
            name='title',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportpresets',
            name='graph_type',
            field=models.CharField(max_length=50),
        ),
    ]