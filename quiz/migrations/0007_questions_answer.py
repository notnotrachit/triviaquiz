# Generated by Django 3.2.5 on 2021-07-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_questions_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]