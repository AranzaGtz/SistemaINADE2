# Generated by Django 5.0.7 on 2024-07-22 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_formatocotizacion_formatoorden_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="concepto",
            name="estado",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ordentrabajo",
            name="concepto",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="oder_trabajo",
                to="accounts.concepto",
            ),
        ),
        migrations.DeleteModel(
            name="Formato",
        ),
    ]