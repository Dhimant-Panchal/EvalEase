from django.urls import include, path

from .views import (
    ConvenerAssignmentViewList,
    ConvenerAssignmentOverviewSubmissionViewList,
    ConvenerSubmissionEvaluationViewList,
    ConvenerSubmissionDetailedView,
    ConvenerSubmissionReccomendationView,
    ConvenerEvaluationView,
    ConvenerAssignmentReportView,
)

urlpatterns = [
    path(
        "assignments",
        ConvenerAssignmentViewList.as_view(),
    ),
    path(
        "assignments/<int:assignment_id>/overview",
        ConvenerAssignmentOverviewSubmissionViewList.as_view(),
    ),
    path(
        "assignments/<int:assignment_id>/report",
        ConvenerAssignmentReportView.as_view(),
    ),
    path(
        "submission/<int:submission_id>/details",
        ConvenerSubmissionDetailedView.as_view(),
    ),
    path(
        "submission/<int:submission_id>/reccomendations",
        ConvenerSubmissionReccomendationView.as_view(),
    ),
    path(
        "submission/<int:submission_id>/evaluations",
        ConvenerSubmissionEvaluationViewList.as_view(),
    ),
    path(
        "evaluation/<int:evaluation_id>",
        ConvenerEvaluationView.as_view(),
    ),
]
