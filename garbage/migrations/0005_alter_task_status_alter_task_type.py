# Generated by Django 4.1.4 on 2023-04-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("garbage", "0004_brigada_operator_remove_task_user_task_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[(1, "Not started"), (2, "In progress"), (3, "Finished")],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="type",
            field=models.CharField(
                choices=[
                    (1, "Install ecobox"),
                    (2, "Empty ecobox"),
                    (3, "Dismantle ecobox"),
                ],
                max_length=255,
            ),
        ),
    ]