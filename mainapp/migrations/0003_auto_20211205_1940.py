# Generated by Django 3.2.9 on 2021-12-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211205_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие sd карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраиваемой памяти'),
        ),
    ]
