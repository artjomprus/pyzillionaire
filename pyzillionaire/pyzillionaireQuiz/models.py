from django.db import models


class TriviaQuestions(models.Model):
	category = models.CharField(max_length=200)
	type = models.CharField(max_length=25)
	difficulty = models.CharField(max_length=10)
	question = models.TextField()
	correct_answer = models.CharField(max_length=300)
	incorrect_answer = models.JSONField()
