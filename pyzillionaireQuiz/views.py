import os
import requests
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .utils.api import fetch_questions
from .models import TriviaQuestion


# def register(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get("username")
# 			messages.success(request, f"You account is created, get onboard!")
# 			return redirect("login")
# 	else:
# 		form = UserCreationForm()
# 	return render(request, "registration/register.html", {"form": form})
#
#
# def user_login(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(data=request.POST)
# 		if form.is_valid():
# 			user = form.get_user()
# 			login(request, user)
# 			messages.success(request, f"Welcome onboard, you are logged in as {user.username}")
# 			return redirect("home")
# 		else:
# 			form = UserCreationForm()
# 		return render(request, "registration/register.html", {"form": form})
#
#
# def logout(request):
# 	logout(request)
# 	messages.success(request, "You are logged out of the system")
# 	return redirect("home")
#
#
# @login_required
# def home(request):
# 	return render(request, "index.html")

def category(request):
	pass


def difficulty(request):
	pass


def all_questions(request):
	response = fetch_questions(request)
	if response.status_code == 200:
		data = response.json()
		results = data.get("results", {"results": "No results"})

		if results:
			for result in results:
				question = TriviaQuestion(
					category=result[0].get("category"),
					type=result[0].get("type"),
					difficulty=result[0].get("difficulty"),
					question=result[0].get("questions"),
				)

	questions = TriviaQuestion.objects.all()
	context = {"questions": questions}
	return
