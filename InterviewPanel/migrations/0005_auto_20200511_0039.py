# Generated by Django 3.0.5 on 2020-05-10 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewPanel', '0004_delete_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='id',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.AddField(
            model_name='answers',
            name='questions_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InterviewPanel.Questions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answers',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]
