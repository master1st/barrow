# Generated by Django 4.1.3 on 2022-11-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_deal', '0003_alter_deal_product_alter_deal_user_cons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='type',
            field=models.CharField(choices=[('01', '직거래만'), ('10', '택배거래만'), ('11', '택배/직거래')], max_length=20),
        ),
    ]