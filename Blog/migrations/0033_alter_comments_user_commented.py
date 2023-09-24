# Generated by Django 4.2.4 on 2023-09-24 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0032_alter_post_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_commented',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]