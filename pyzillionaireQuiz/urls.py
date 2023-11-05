from django.urls import path

from .views import all_questions
from .views import index


urlpatterns = [
    path("all/", all_questions),
    path("", index),
]
