# Generated by Django 3.2.13 on 2022-07-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='Default.jpg', upload_to='blog/'),
        ),
    ]
