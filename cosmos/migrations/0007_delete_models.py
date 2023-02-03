# Generated by Django 3.2.7 on 2021-10-13 17:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cosmos", "0006_delete_foreign_keys"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Partner",
                ),
                migrations.DeleteModel(
                    name="Testimonial",
                ),
                migrations.DeleteModel(
                    name="FileObject",
                ),
                migrations.DeleteModel(
                    name="GMM",
                ),
                migrations.DeleteModel(
                    name="News",
                ),
                migrations.DeleteModel(
                    name="PhotoAlbum",
                ),
                migrations.DeleteModel(
                    name="PhotoObject",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Partner",
                    table="core_partner",
                ),
                migrations.AlterModelTable(
                    name="Testimonial",
                    table="core_testimonial",
                ),
                migrations.AlterModelTable(
                    name="FileObject",
                    table="core_fileobject",
                ),
                migrations.AlterModelTable(
                    name="GMM",
                    table="core_gmm",
                ),
                migrations.AlterModelTable(
                    name="News",
                    table="core_news",
                ),
                migrations.AlterModelTable(
                    name="PhotoAlbum",
                    table="core_photoalbum",
                ),
                migrations.AlterModelTable(
                    name="PhotoObject",
                    table="core_photoobject",
                ),
            ],
        ),
    ]
