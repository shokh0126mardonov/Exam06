from django.urls import path

from .views import ScoriesView

urlpatterns = [
    path('scores/',ScoriesView.as_view(),name='score_page'),
    path('scores/<int:id>/',ScoriesView.as_view(),name='detail_score'),
]
