from django.db import models


class TriviaQuestion(models.Model):
	category = models.CharField(max_length=200)
	type = models.CharField(max_length=25)
	difficulty = models.CharField(max_length=10)
	question = models.TextField()
	answer_set = models.ForeignKey('AnswerSet', null=False, blank=False, on_delete=models.CASCADE)


class AnswerSet(models.Model):
	correct_answer = models.CharField(max_length=300, blank=False, null=False)
	incorrect_answer_1 = models.CharField(max_length=300, blank=False, null=False)
	incorrect_answer_2 = models.CharField(max_length=300, blank=False, null=False)
	incorrect_answer_3 = models.CharField(max_length=300, blank=False, null=False)


class Category:
	pass


class Difficulty:
	pass
