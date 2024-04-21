from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, authentication, views

from unidb.cworker.models import Module, StudentProfile, Assignment, Submission, Keyword
from unidb.cworker.serializers import ModuleSerializer, AssignmentSerializer
from .serializers import StudentSubmissionSerializer


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "studentprofile")
        )


class StudentModuleViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudent]
    serializer_class = ModuleSerializer
    lookup_url_kwarg = "module_id"

    def get_queryset(self):
        return self.request.user.studentprofile.modules


class StudentAssignmentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assignment.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudent]
    serializer_class = AssignmentSerializer
    lookup_url_kwarg = "assignment_id"

    def get_queryset(self):
        # TODO: Doesn't verify the querying user is actually in the module!
        return self.queryset.filter(module_id=self.kwargs["module_id"])


# https://browniebroke.com/blog/nested-viewsets-with-django-rest-framework/


class StudentSubmissionViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudent]
    serializer_class = StudentSubmissionSerializer
    lookup_url_kwarg = "submission_id"

    def get_queryset(self):
        return self.request.user.studentprofile.submission_set

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.studentprofile)


class StudentAssignmentSubmissionView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request, assignment_id, format=None):
        assignment = get_object_or_404(Assignment, id=assignment_id)

        if assignment.module in request.user.studentprofile.modules.all():
            [submission, created] = Submission.objects.get_or_create(
                assignment=assignment, creator=request.user.studentprofile
            )
            return views.Response(submission.id)
