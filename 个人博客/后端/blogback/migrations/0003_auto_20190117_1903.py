# Generated by Django 2.1.5 on 2019-01-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogback', '0002_auto_20190115_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=20, unique=True, verbose_name='文章标题')),
                ('art_content', models.TextField(verbose_name='文章内容')),
                ('art_keywords', models.CharField(max_length=20, unique=True, verbose_name='关键字')),
                ('art_describe', models.CharField(max_length=255, unique=True, verbose_name='描述')),
            ],
            options={
                'db_table': 'f_article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=20, unique=True, verbose_name='栏目名称')),
                ('cate_alias', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='栏目别名')),
                ('cate_keywords', models.CharField(max_length=10, unique=True, verbose_name='关键字')),
                ('cate_describe', models.CharField(max_length=255, unique=True, verbose_name='描述')),
                ('cate_fid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogback.Category', verbose_name='父节点')),
            ],
            options={
                'db_table': 'f_category',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='article',
            name='art_cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blogback.Category', verbose_name='栏目'),
        ),
    ]
