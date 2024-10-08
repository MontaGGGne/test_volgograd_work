# Generated by Django 2.2.2 on 2024-08-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, ''), (1, 'Мужской'), (2, 'Женский')], default=0, verbose_name='Пол')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Физическое лицо',
                'verbose_name_plural': 'Физические лица',
            },
        ),
    ]
