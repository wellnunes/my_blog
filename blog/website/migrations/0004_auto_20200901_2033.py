# Generated by Django 3.1 on 2020-09-01 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]
