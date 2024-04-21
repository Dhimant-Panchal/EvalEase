from django.urls import path

from .views import KeywordSearchView

urlpatterns = [
    path(r"search/<str:query>/", KeywordSearchView.as_view()),
]
