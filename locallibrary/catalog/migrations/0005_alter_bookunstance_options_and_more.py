# Generated by Django 4.2.1 on 2023-05-03 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_remove_author_nacionalidade"),
    ]

    operations = [
        migrations.AlterModelOptions(name="bookunstance", options={},),
        migrations.RemoveField(model_name="bookunstance", name="due_back",),
    ]
