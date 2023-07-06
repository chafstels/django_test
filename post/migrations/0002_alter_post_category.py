# Generated by Django 4.2.2 on 2023-07-05 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                related_query_name="posts",
                to="post.category",
            ),
        ),
    ]