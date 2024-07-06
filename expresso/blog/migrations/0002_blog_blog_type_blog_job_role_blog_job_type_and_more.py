# Generated by Django 5.0.6 on 2024-07-06 07:18

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_type",
            field=models.CharField(
                choices=[("INTERVIEW", "Interview"), ("WORK EXP", "Work Experience")],
                default="INTERVIEW",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="job_role",
            field=models.CharField(
                choices=[
                    ("DEV", "Developer"),
                    ("DES", "Designer"),
                    ("MKT", "Marketing"),
                ],
                default="DEV",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("FT", "Full Time"),
                    ("PT", "Part Time"),
                    ("INTERN", "Internship"),
                ],
                default="FT",
                max_length=6,
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="organization",
            field=models.CharField(
                default=datetime.datetime(
                    2024, 7, 6, 7, 18, 29, 914800, tzinfo=datetime.timezone.utc
                ),
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="user_type",
            field=models.CharField(
                choices=[("STUD", "Student"), ("PROF", "Professional")],
                default="STUD",
                max_length=4,
            ),
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("college", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
