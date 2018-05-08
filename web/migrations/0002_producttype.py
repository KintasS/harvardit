# Generated by Django 2.0.4 on 2018-04-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyperledger_traceit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=255)),
            ],
        ),
    ]