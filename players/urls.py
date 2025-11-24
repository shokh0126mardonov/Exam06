from django.urls import path

from .views import PlayerView

urlpatterns = [
    path('players/',PlayerView.as_view(),name='players'),
    path('players/<int:id>/',PlayerView.as_view(),name='player_detail'),
]
