# Generated by Django 2.1.7 on 2019-02-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojinha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
        ),
    ]
