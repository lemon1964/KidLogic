# Generated by Django 4.2.4 on 2023-08-12 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("item_DRF", "0002_delete_objec"),
    ]

    operations = [
        migrations.CreateModel(
            name="Objec",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("picture", models.CharField(max_length=40)),
                ("sound", models.CharField(max_length=40)),
                ("ident", models.BooleanField(default=True)),
                (
                    "grup",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="objecs",
                        to="item_DRF.grup",
                    ),
                ),
            ],
        ),
    ]
