import requests


def fetch_questions(category, difficulty):
	url = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}&type=multiple&encode=url3986"
	response = requests.get(url)
