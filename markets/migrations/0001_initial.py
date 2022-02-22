# Generated by Django 4.0.2 on 2022-02-15 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('name', models.CharField(max_length=100, verbose_name='마켓이름')),
                ('site_url', models.URLField(max_length=100, verbose_name='마켓사이트URL')),
                ('email', models.EmailField(max_length=100, verbose_name='마켓대표이메일')),
                ('review_point', models.FloatField(default=0, verbose_name='리뷰평점')),
                ('description', models.TextField(verbose_name='설명')),
                ('master', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'verbose_name': '마켓',
                'verbose_name_plural': '마켓들',
                'ordering': ('-id',),
            },
        ),
    ]
