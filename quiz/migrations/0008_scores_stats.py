# Generated by Django 3.2.5 on 2021-07-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_questions_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='stats',
            field=models.CharField(default='', max_length=99999),
            preserve_default=False,
        ),
    ]