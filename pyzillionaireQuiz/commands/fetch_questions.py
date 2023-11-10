
from django.core.management.base import BaseCommand
import requests
from pyzillionaireQuiz.models import TriviaQuestions


class Command(BaseCommand):
    help = 'Fetch questions from API and store in the database'

    def handle(self, *args, **kwargs):
        api_url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple&encode=url3986'
        response = requests.get(api_url)
        questions_data = response.json()

        for question_data in questions_data:
            TriviaQuestions.objects.create(question_text=question_data['text'])

        self.stdout.write(self.style.SUCCESS('Questions fetched and stored successfully'))
