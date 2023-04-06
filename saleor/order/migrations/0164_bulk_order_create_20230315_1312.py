# Generated by Django 3.2.18 on 2023-03-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0163_order_events_rename_transaction_events"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ("-number",),
                "permissions": (
                    ("manage_orders", "Manage orders."),
                    ("manage_orders_import", "Manage orders import"),
                ),
            },
        ),
        migrations.AlterField(
            model_name="order",
            name="origin",
            field=models.CharField(
                choices=[
                    ("checkout", "Checkout"),
                    ("draft", "Draft"),
                    ("reissue", "Reissue"),
                    ("bulk_create", "Bulk create"),
                ],
                max_length=32,
            ),
        ),
    ]