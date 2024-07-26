# Generated by Django 5.0.7 on 2024-07-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_ordentrabajoconcepto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="moneda",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MXN", "MXN - Moneda Nacional Mexicana"),
                    ("USD", "USD - Dolar Estadunidense"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]