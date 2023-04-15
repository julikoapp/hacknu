# Generated by Django 4.1.4 on 2023-04-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("garbage", "0003_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brigada",
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
                ("title", models.CharField(max_length=255)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Operator",
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
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("phone", models.IntegerField()),
                ("address", models.CharField(max_length=255)),
                ("is_staff", models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="task",
            name="user",
        ),
        migrations.AddField(
            model_name="task",
            name="type",
            field=models.CharField(
                choices=[
                    (1, "Установить экобокс"),
                    (2, "Вывезти мусор"),
                    (3, "Демонтировать экобокс"),
                ],
                default=1,
                max_length=255,
            ),
            preserve_default=False,
        ),
    ]