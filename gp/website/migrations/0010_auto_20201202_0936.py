# Generated by Django 3.0 on 2020-12-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_portfolio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
