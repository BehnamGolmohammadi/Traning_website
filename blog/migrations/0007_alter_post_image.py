# Generated by Django 3.2.13 on 2022-07-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='blog/Default.png', upload_to='blog/'),
        ),
    ]
