# Generated by Django 3.0.5 on 2020-06-08 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewPannel', '0008_auto_20200511_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='InterviewPannel.Quiz'),
            preserve_default=False,
        ),
    ]
