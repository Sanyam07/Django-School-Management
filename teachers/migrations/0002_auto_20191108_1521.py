# Generated by Django 2.2.7 on 2019-11-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Designation'),
        ),
    ]
