from django.urls import include, path
from rest_framework import routers

from .views import (
    StudentAssignmentSubmissionView,
    StudentModuleViewSet,
    StudentAssignmentsViewSet,
    StudentSubmissionViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"modules",
    StudentModuleViewSet,
    basename="module",
)
router.register(
    r"modules/(?P<module_id>[^/.]+)/assignments",
    StudentAssignmentsViewSet,
    basename="module-assignment",
)
router.register(
    r"submissions",
    StudentSubmissionViewSet,
    basename="submission",
)

urlpatterns = [
    path(
        "assignments/<int:assignment_id>/submission/",
        StudentAssignmentSubmissionView.as_view(),
    ),
    path("", include(router.urls)),
]
