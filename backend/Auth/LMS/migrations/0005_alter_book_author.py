# Generated by Django 4.1.7 on 2023-02-23 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("LMS", "0004_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="LMS.author",
            ),
        ),
    ]
