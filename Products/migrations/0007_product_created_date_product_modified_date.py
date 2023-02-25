# Generated by Django 4.1.7 on 2023-02-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]