from django.urls import path

from .views import all_questions

urlpatterns = [
    path("all/", all_questions),
]
