# Generated by Django 4.1.7 on 2023-03-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_alter_student_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="user_type",
            field=models.CharField(default="STUDENT", max_length=255),
        ),
    ]