# Generated by Django 5.0 on 2024-06-15 14:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('annotation', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('published', models.DateField()),
            ],
        ),
    ]
