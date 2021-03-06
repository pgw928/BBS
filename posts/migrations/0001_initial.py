# Generated by Django 3.0.3 on 2020-08-07 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('title', models.CharField(default='', max_length=50, verbose_name='글제목')),
                ('contents', models.TextField(max_length=1000, verbose_name='글내용')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='댓글 작성자')),
                ('contents', models.TextField(max_length=1000, verbose_name='댓글 내용')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]
