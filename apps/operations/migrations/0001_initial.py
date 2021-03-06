# Generated by Django 2.0.5 on 2018-05-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('weight', models.IntegerField(default=1, verbose_name='广告权重')),
                ('image', models.ImageField(upload_to='advertise/%Y/%m', verbose_name='广告图片')),
                ('is_approval', models.BooleanField(default=False, verbose_name='审批状态')),
            ],
            options={
                'verbose_name': '广告信息',
                'verbose_name_plural': '广告信息',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='访问顺序')),
                ('is_approval', models.BooleanField(default=False, verbose_name='审批状态')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱地址')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('verify_code', models.CharField(default=0, max_length=100, verbose_name='邮箱验证码')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '忘记密码'), ('verify_id', '实名认证')], default='register', max_length=20, verbose_name='验证码类型')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户关注',
                'verbose_name_plural': '用户关注',
            },
        ),
        migrations.CreateModel(
            name='UserSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_no', models.CharField(max_length=40, verbose_name='订单编号')),
                ('support_nums', models.IntegerField(default=1, verbose_name='回报数量')),
            ],
            options={
                'verbose_name': '用户支持',
                'verbose_name_plural': '用户支持',
            },
        ),
    ]
