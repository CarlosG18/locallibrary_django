# Generated by Django 4.2.1 on 2023-05-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_language_book_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="nacionalidade",
            field=models.CharField(
                choices=[
                    ("bra", "Brasileiro"),
                    ("usa", "Americano"),
                    ("fra", "Frances"),
                ],
                help_text="escolha a nacionalidade do autor",
                max_length=3,
                null=True,
            ),
        ),
    ]
