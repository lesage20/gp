# Generated by Django 3.0 on 2020-12-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='desciption',
            field=models.TextField(default='Veuillez enregistrer votre email pour ne rein rater '),
        ),
    ]