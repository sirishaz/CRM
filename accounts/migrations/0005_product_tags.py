# Generated by Django 4.2.6 on 2023-10-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
