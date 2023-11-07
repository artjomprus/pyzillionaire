from django.urls import path
from . import views



urlpatterns = [
    path('all/', views.all_questions, name='all_questions'),
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),

]


# urlpatterns = [
#     path("all/", all_questions),
# ]
