# Generated by Django 4.2.7 on 2023-11-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0003_alter_fotografia_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="fotografia",
            name="descricao",
            field=models.TextField(default="Ainda sem descrição..."),
        ),
    ]
