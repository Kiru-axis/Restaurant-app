# Generated by Django 3.2.5 on 2021-08-02 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.category'),
        ),
    ]