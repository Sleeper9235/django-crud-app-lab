# Generated by Django 5.1 on 2024-08-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_alter_group_placeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='placeholder',
            field=models.CharField(default=' ', editable=False, max_length=100),
        ),
    ]
