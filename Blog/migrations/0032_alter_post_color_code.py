# Generated by Django 4.2.4 on 2023-09-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0031_post_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color_code',
            field=models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], default='red', max_length=10),
        ),
    ]
