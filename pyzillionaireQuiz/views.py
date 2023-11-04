import requests

from utils.api import fetch_questions
from .models import TriviaQuestion


def all_questions(request):
	response = fetch_questions()

	if response.status_code == 200:
		data = response.json()
		results = data.get("results", {"results": "No results"})

		if results:
			for result in results:
				question = TriviaQuestion(
					category=result.get("category"),
					type=result.get("type"),
					difficulty=result.get("difficulty"),
					question=result.get("questions"),

				)
				question.save()

	questions = TriviaQuestion.objects.all()
	context = {"questions": questions}
	return
