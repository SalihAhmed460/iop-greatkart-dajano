# Generated by Django 5.1 on 2024-09-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
