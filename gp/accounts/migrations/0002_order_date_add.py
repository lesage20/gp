# Generated by Django 3.0.7 on 2020-06-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
