from django.urls import include, path
from rest_framework import routers

from .views import (
    AcademicProfileView,
    AcademicViewSet,
    AcademicEvaluationInboxListView,
    AcademicEvaluationSubmitView,
)

router = routers.DefaultRouter()
router.register(r"profiles", AcademicViewSet, basename="academic")

urlpatterns = [
    path("myprofile", AcademicProfileView.as_view()),
    path("inbox", AcademicEvaluationInboxListView.as_view()),
    path("submit/<int:evaluation_id>", AcademicEvaluationSubmitView.as_view()),
    path("", include(router.urls)),
]
