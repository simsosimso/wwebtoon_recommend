# Generated by Django 4.0.6 on 2022-07-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_kakaopagedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='KakaowebtoonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]
