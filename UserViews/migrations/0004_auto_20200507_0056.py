# Generated by Django 3.0.5 on 2020-05-06 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserViews', '0003_auto_20200501_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test1',
            name='id',
        ),
        migrations.AlterField(
            model_name='test1',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
