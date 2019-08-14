# Generated by Django 2.0.3 on 2018-07-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpkart', '0006_auto_20180714_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('town', models.CharField(max_length=300)),
                ('zipcode', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('comment', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'myuser',
            },
        ),
    ]
