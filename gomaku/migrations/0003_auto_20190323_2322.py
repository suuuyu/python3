# Generated by Django 2.1.7 on 2019-03-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomaku', '0002_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me', models.IntegerField()),
                ('friend', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me', models.IntegerField()),
                ('opponent', models.IntegerField()),
                ('win', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(default=''),
        ),
    ]
