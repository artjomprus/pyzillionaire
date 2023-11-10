# Generated by Django 4.2.6 on 2023-11-10 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyzillionaireQuiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=300)),
                ('incorrect_answer_1', models.CharField(max_length=300)),
                ('incorrect_answer_2', models.CharField(max_length=300)),
                ('incorrect_answer_3', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TriviaQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=25)),
                ('difficulty', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('answer_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyzillionaireQuiz.answerset')),
            ],
        ),
        migrations.DeleteModel(
            name='TriviaQuestions',
        ),
    ]
