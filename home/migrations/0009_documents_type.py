# Generated by Django 3.2.6 on 2021-08-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='type',
            field=models.CharField(choices=[('Documents', 'Documents'), ('Drivers Aplications', 'Drivers Aplications'), ('Existiong Trucks Docs', 'Existiong Trucks Docs')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
