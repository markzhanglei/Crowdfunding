# Generated by Django 2.0.5 on 2018-05-15 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayorder',
            name='address',
            field=models.ForeignKey(on_delete='cascade', to='users.UserAddress', verbose_name='收货地址'),
        ),
        migrations.AddField(
            model_name='userpayorder',
            name='item',
            field=models.ForeignKey(on_delete='cascade', to='projects.ProjectItem', verbose_name='支持回报'),
        ),
        migrations.AddField(
            model_name='userpayorder',
            name='user',
            field=models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
