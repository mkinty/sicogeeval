# Generated by Django 4.0.1 on 2023-02-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quiz_other_formation1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='acquis1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='acquis2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='acquis3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='acquis_comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
