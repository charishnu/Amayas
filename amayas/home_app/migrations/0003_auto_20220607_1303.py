# Generated by Django 2.2 on 2022-06-07 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
