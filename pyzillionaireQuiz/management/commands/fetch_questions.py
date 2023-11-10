
from django.core.management.base import BaseCommand
import requests
from pyzillionaireQuiz.models import TriviaQuestion


class Command(BaseCommand):
    help = 'Fetch questions from API and store in the database'

    def handle(self, *args, **kwargs):
        api_url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple&encode=url3986'
        response = requests.get(api_url)
        data = response.json()

        # Check if 'results' key is present in the response
        if 'results' in data:
            questions_data = data['results']

            for question_data in questions_data:
                TriviaQuestion.objects.create(question_text=question_data['question'])
            self.stdout.write(self.style.SUCCESS('Questions fetched and stored successfully'))
        else:
            self.stdout.write(self.style.ERROR('No "results" key in API response'))
