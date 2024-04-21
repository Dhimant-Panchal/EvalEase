from django.shortcuts import get_object_or_404, get_list_or_404
import statistics

from rest_framework import (
    permissions,
    generics,
    authentication,
    views,
    response,
)

from unidb.cworker.models import Module, Assignment, Submission, Evaluation
from unidb.academic.views import reccomendAcademics
from .serializers import (
    ConvenerAssignmentSerializer,
    ConvenerSubmissionSerializer,
    ConvenerEvaluationSerializer,
)


class IsConvener(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "convenerprofile")
        )


class IsModuleConvener(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            module = Module.get(id=view.kwargs["module_id"])
            return bool(request.user.convenerprofile in module.convener_set)
        except:
            return False


class IsAssignmentConvener(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            assignment = Assignment.objects.get(id=view.kwargs["assignment_id"])
            module = assignment.module
            return request.user.convenerprofile in module.convenerprofile_set.all()
        except:
            return False


class IsSubmissionConvener(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            submission = Submission.objects.get(id=view.kwargs["submission_id"])
            module = submission.assignment.module
            return request.user.convenerprofile in module.convenerprofile_set.all()
        except:
            return False


class IsEvaluationConvener(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            evaluation = Evaluation.objects.get(id=view.kwargs["evaluation_id"])
            module = evaluation.submission.assignment.module
            return request.user.convenerprofile in module.convenerprofile_set.all()
        except:
            return False


class ConvenerAssignmentViewList(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener]
    serializer_class = ConvenerAssignmentSerializer

    def get_queryset(self):
        # TODO: Cleanup, use functional!
        q = []
        for d in self.request.user.convenerprofile.modules.all():
            q.extend(d.assignments.all())
        return q


class ConvenerAssignmentOverviewSubmissionViewList(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsAssignmentConvener]
    serializer_class = ConvenerSubmissionSerializer
    lookup_url_kwarg = "assignment_id"

    def get_queryset(self):
        assignment = Assignment.objects.get(id=self.kwargs["assignment_id"])
        return assignment.submission_set


class ConvenerSubmissionDetailedView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsSubmissionConvener]
    serializer_class = ConvenerSubmissionSerializer
    lookup_url_kwarg = "submission_id"

    def get_object(self):
        return Submission.objects.get(id=self.kwargs["submission_id"])


class ConvenerSubmissionReccomendationView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsSubmissionConvener]
    serializer_class = ConvenerSubmissionSerializer
    lookup_url_kwarg = "submission_id"

    def get(self, request, submission_id):
        submission = Submission.objects.get(id=self.kwargs["submission_id"])
        querySet = set()
        for v in submission.keywords.all():
            querySet.add(v.text)
        return response.Response(reccomendAcademics(querySet))


class ConvenerSubmissionEvaluationViewList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsSubmissionConvener]
    serializer_class = ConvenerEvaluationSerializer
    lookup_url_kwarg = "submission_id"

    def perform_create(self, serializer):
        submission = Submission.objects.get(id=self.kwargs["submission_id"])
        serializer.save(submission=submission)

    def get_queryset(self):
        submission = Submission.objects.get(id=self.kwargs["submission_id"])
        return submission.evaluation_set


class ConvenerEvaluationView(generics.RetrieveDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsEvaluationConvener]
    serializer_class = ConvenerEvaluationSerializer
    lookup_url_kwarg = "evaluation_id"
    queryset = Evaluation.objects.all()


class ConvenerAssignmentReportView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsConvener, IsAssignmentConvener]

    def get(self, request, assignment_id):
        assignment = Assignment.objects.get(id=assignment_id)

        scores = []

        for sub in assignment.submission_set.all():
            for ev in sub.evaluation_set.all():
                if ev.mark:
                    scores.append(ev.mark)

        if len(scores) < 2:
            return response.Response({})

        allStdDev = statistics.stdev(scores)
        allMean = statistics.fmean(scores)

        outliers = []

        for sub in assignment.submission_set.all():
            myScores = []
            for ev in sub.evaluation_set.all():
                if ev.mark:
                    myScores.append(ev.mark)

            if len(myScores) > 0:
                myAverage = statistics.fmean(myScores)
                if abs(myAverage - allMean) > 2.5 * allStdDev:
                    outliers.append(
                        {
                            "score": myAverage,
                            "submission": ConvenerSubmissionSerializer(sub).data,
                        }
                    )

        return response.Response(
            {
                "all_std_dev": allStdDev,
                "all_mean": allMean,
                "outliers": outliers,
            }
        )
