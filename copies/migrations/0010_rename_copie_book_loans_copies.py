# Generated by Django 4.2.1 on 2023-05-05 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0009_alter_book_loans_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book_loans",
            old_name="copie",
            new_name="copies",
        ),
    ]
