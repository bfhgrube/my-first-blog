# Generated by Django 3.1.4 on 2020-12-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locus',
            name='landkreis',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
