# Generated by Django 5.0.6 on 2024-06-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chaivarity_type_alter_chaivarity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
