# Generated by Django 3.0.5 on 2020-05-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quizdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
    ]