# Generated by Django 5.0 on 2024-06-16 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover_alter_book_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
