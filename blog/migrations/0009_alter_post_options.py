# Generated by Django 3.2.14 on 2022-07-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220714_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-Created_Date']},
        ),
    ]