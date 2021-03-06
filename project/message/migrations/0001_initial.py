# Generated by Django 3.0.6 on 2021-01-07 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False, verbose_name='メッセージid')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='件名')),
                ('message', models.TextField(max_length=255, verbose_name='メッセージ詳細')),
                ('message_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='送信日時')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_user', to=settings.AUTH_USER_MODEL, verbose_name='送信ユーザー')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_user', to=settings.AUTH_USER_MODEL, verbose_name='受信ユーザー')),
            ],
        ),
    ]
