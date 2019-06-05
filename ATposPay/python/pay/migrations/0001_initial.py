# Generated by Django 2.1.7 on 2019-05-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('buyerid', models.IntegerField()),
                ('methodid', models.IntegerField()),
            ],
            options={
                'db_table': 'pay',
            },
        ),
    ]
