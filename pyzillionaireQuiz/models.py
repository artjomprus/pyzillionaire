from django.db import models


#  Create your models here.
class TriviaQuestion(models.Model):
    category = models.CharField(
       max_length=200,
       blank=False,
       null=False
    )
    type = models.CharField(
       max_length=25,
       blank=False,
       null=False
    )
    difficulty = models.CharField(
       max_length=10,
       blank=False,
       null=False
    )
    question = models.TextField(
       blank=False,
       null=False
    )
    answer_set = models.ForeignKey(
       'AnswerSet',
       null=False,
       blank=False,
       on_delete=models.CASCADE
    )
    difficulty_level = models.ForeignKey(
       'DifficultyLevel',
       null=True,
       blank=False,
       on_delete=models.CASCADE
    )
    category_list = models.ForeignKey(
       'CategoryList',
       null=True,
       blank=False,
       on_delete=models.CASCADE
    )
    Amount = models.ForeignKey(
       'Amount',
       null=False,
       blank=False,
       on_delete=models.CASCADE
    )

    class AnswerSet(models.Model):
       correct_answer = models.CharField(
          max_length=300,
          blank=False,
          null=False
       )
       incorrect_answer_1 = models.CharField(
          max_length=300,
          blank=False,
          null=False
       )
       incorrect_answer_2 = models.CharField(
          max_length=300,
          blank=False,
          null=False
       )
       incorrect_answer_3 = models.CharField(
          max_length=300,
          blank=False,
          null=False,

       )
       TriviaQuestion = models.ForeignKey(
          'TriviaQuestion',
          null=False,
          blank=False,
          on_delete=models.CASCADE

       )


class CategoryList(models.Model):
    category_id = models.CharField(max_length=5, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    TriviaQuestion = models.ForeignKey(
       'TriviaQuestion',
       null=True,
       blank=False,
       on_delete=models.CASCADE,
    )


class DifficultyLevel(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    difficulty_choices = [
       (EASY, 'easy'),
       (MEDIUM, 'medium'),
       (HARD, 'hard')
    ]
    level = models.CharField(
       max_length=10,
       choices=difficulty_choices,
       default=EASY,
       unique=True,
       null=False,
       blank=False)
    TriviaQuestion = models.ForeignKey(
       'TriviaQuestion',
       null=True,
       blank=False,
       on_delete=models.CASCADE,
    )


# TriviaQuestion = models.ForeignKey('TriviaQuestion', on_delete=models.CASCADE, null=False, blank=False)
class Amount(models.Model):
    value = models.IntegerField()

    def __str__(self):
       return str(self.value)