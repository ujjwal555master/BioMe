# Generated by Django 4.2.10 on 2024-03-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='allabout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=23)),
                ('coin', models.IntegerField(default=0)),
            ],
        ),
    ]
