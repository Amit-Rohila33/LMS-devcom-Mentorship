# Generated by Django 4.1.7 on 2023-03-01 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("LMS", "0013_remove_book_genre_book_genre"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="Genre",
            new_name="genre",
        ),
    ]
