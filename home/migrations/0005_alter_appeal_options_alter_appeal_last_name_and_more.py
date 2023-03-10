# Generated by Django 4.0.8 on 2022-12-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_appeal_last_name_alter_appeal_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appeal',
            options={'verbose_name': 'Обращение', 'verbose_name_plural': 'Обращения'},
        ),
        migrations.AlterField(
            model_name='appeal',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='option',
            field=models.IntegerField(choices=[(1, 'SOS размещение'), (2, 'Гуманитарная помощь'), (3, 'Необходим адресный сбор'), (4, 'Koнсультация психолога'), (5, 'Консультация юриста'), (6, 'Хочу в группу поддержки'), (7, 'Хочу быть волонтером фонда')], verbose_name='Тип требуемой помощи'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='type',
            field=models.IntegerField(choices=[(1, 'Помощь'), (2, 'Консультация'), (3, 'Волонтерство')], verbose_name='Тип обращения'),
        ),
    ]
