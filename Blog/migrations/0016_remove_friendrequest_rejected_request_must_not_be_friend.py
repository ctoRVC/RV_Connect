# Generated by Django 4.2.4 on 2023-08-13 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_customuser_remove_friendship_friend_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='friendrequest',
            name='rejected_request_must_not_be_friend',
        ),
    ]
