# Generated by Django 4.2.9 on 2024-01-25 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]