from django.core.management.base import BaseCommand
import requests
from pyzillionaire.pyzillionaireQuiz.models import TriviaQuestions


class Command(BaseCommand):
	help = 'Fetch and save trivia data from the OpenTDB API'

	def handle(self, *args, **options):
		url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple&encode=url3986"
		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			results = data.get("results")

			if results:
				for result in results:
					question = TriviaQuestions(
						category=result["category"],
						type=result["type"],
						difficulty=result["difficulty"],
						question=result["question"],
						correct_answer=result["correct_answer"],
						incorrect_answers=result["incorrect_answers"]
					)
					question.save()
					self.stdout.write(self.style.SUCCESS('Successfully fetched and saved trivia data'))
			else:
				self.stdout.write(self.style.ERROR('No results found in the API response'))
		else:
			self.stdout.write(self.style.ERROR('Failed to fetch trivia data from the API'))
