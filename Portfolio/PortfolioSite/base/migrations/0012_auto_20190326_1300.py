# Generated by Django 2.1.7 on 2019-03-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20190326_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='Example: Alfredemmanuelinyang@gmail.com', max_length=254),
        ),
    ]
