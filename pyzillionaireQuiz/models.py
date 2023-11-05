from django.db import models


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
		null=False
	)


class Category(models.Model):
	category_id = models.CharField(max_length=5, null=False, blank=False)
	name = models.CharField(max_length=50, null=False, blank=False)


class Difficulty(models.Model):
	level = models.CharField(max_length=10, null=False, blank=False)

