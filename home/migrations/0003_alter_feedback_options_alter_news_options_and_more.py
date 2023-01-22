# Generated by Django 4.0.8 on 2022-11-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_add_email_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='programs',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='programs',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]