import requests
from django.http import JsonResponse

# def fetch_category_names():
# 	url = "https://opentdb.com/api_category.php"
# 	response = requests.get(url)
# 	if response.status_code == 200:
# 		data = response.json()
# 		categories = data.get("trivia_categories", [])
# 		return categories
# 	return []


def fetch_questions(request):
	amount = requests.get("amount")
	category = requests.get("category")
	difficulty = requests.get("difficulty")
	if not amount or not category or not difficulty:
		return JsonResponse({"error": "missing parameters"}, status=400)
	url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
	response = requests.get(url)
