# Generated by Django 4.1.3 on 2022-11-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_home_content_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_content',
            name='IMAGE',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Изображение'),
        ),
    ]
