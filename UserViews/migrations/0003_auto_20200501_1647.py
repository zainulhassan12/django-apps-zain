# Generated by Django 3.0.5 on 2020-05-01 11:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserViews', '0002_auto_20200429_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Domicile',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='Father_Name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='First_Name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='Last_Name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='First_Name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='First_NameF',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.AlterField(
            model_name='userapplication',
            name='Last_NameF',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-z]+([\\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')]),
        ),
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
