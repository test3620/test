# Generated by Django 5.0.2 on 2024-03-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membre', '0005_alter_membres_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membres',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images', verbose_name='IMAGE :'),
        ),
    ]
