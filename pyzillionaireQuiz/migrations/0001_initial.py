# Generated by Django 4.2.6 on 2023-11-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TriviaQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=25)),
                ('difficulty', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('correct_answer', models.CharField(max_length=300)),
                ('incorrect_answer', models.JSONField()),
            ],
        ),
    ]
