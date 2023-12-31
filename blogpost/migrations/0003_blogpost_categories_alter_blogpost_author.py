# Generated by Django 4.2.4 on 2023-08-27 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('accounts', '0001_initial'),
        ('blogpost', '0002_alter_blogpost_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='category.category'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]
