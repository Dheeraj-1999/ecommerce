# Generated by Django 2.0.3 on 2018-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpkart', '0007_mysiteuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
