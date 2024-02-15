# Generated by Django 5.0.2 on 2024-02-15 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZenSpelling', '0002_tile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='correct_answer', to='ZenSpelling.answer'),
        ),
    ]
