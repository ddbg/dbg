# Generated by Django 3.2.4 on 2021-08-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='gravestone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
