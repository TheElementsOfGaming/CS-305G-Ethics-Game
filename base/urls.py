from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="start_home"),
	path('home/', views.home, name="home"),
	path('mainpage/', views.mainpage, name="game_start"),
	path('settings/', views.settings, name="settings"),
	path('leaderboards/', views.leaderboards, name="leaderboards"),
	path('instructions/', views.instructions, name="instructions")
]