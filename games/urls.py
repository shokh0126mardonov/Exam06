from django.urls import path

from .views import GameView

urlpatterns = [
    path('game/<int:id>/',GameView.as_view(),name='game_page_list'),
    path('game/',GameView.as_view(),name='game_page'),
]
