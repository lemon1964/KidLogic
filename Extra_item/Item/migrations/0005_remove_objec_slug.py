# Generated by Django 4.2.4 on 2023-08-11 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Item", "0004_alter_grup_slug"),
    ]

    operations = [
        migrations.RemoveField(model_name="objec", name="slug",),
    ]
