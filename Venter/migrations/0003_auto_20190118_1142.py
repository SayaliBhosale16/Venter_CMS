# Generated by Django 2.1.2 on 2019-01-18 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0002_auto_20190118_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='organisation_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Venter.Organisation'),
        ),
    ]