# Generated by Django 4.2.1 on 2023-05-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_rename_book_id_followings_book_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
