# Generated by Django 3.2.5 on 2021-07-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20210726_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='category',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option1',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option2',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='scores',
            name='q_attempted',
            field=models.CharField(default='[]', max_length=99999),
        ),
    ]