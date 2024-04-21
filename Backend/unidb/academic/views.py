from rest_framework import (
    views,
    viewsets,
    generics,
    permissions,
    response,
    authentication,
)
from itertools import islice

from unidb.cworker.models import AcademicProfile, Evaluation
from unidb.wkeyword.models import Keyword
from unidb.convener.serializers import ConvenerEvaluationSerializer
from .serializers import AcademicProfileSerializer


class IsAcademic(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "academicprofile")
        )


class IsEvaluationAcademic(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            evaluation = Evaluation.objects.get(id=view.kwargs["evaluation_id"])
            return evaluation.marker == request.user.academicprofile
        except:
            return False


class AcademicProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAcademic]
    serializer_class = AcademicProfileSerializer

    def get_object(self):
        return self.request.user.academicprofile


def getOverlap(aca: AcademicProfile, query: set[str]):
    count = 0
    for k in aca.interests.all():
        if k.text in query:
            count += 1
    return count


def reccomendAcademics(querySet: set[str]):
    sortedAcademics = sorted(
        AcademicProfile.objects.all(),
        key=lambda o: getOverlap(o, querySet),
        reverse=True,
    )
    return map(
        lambda o: {
            "overlap": getOverlap(o, querySet),
            "academic": AcademicProfileSerializer(o).data,
        },
        islice(sortedAcademics, 4),
    )


class AcademicInterestsReccomendView(views.APIView):
    def get(self, request):
        querySet = set(self.request.GET.getlist("q", []))
        return response.Response(reccomendAcademics(querySet))


class AcademicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AcademicProfileSerializer
    queryset = AcademicProfile.objects.all()


class AcademicEvaluationInboxListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAcademic]
    serializer_class = ConvenerEvaluationSerializer

    def get_queryset(self):
        return self.request.user.academicprofile.evaluation_set.filter(mark=None).all()


class AcademicEvaluationSubmitView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAcademic, IsEvaluationAcademic]

    def put(self, request, evaluation_id):
        evaluation = Evaluation.objects.get(id=evaluation_id)
        value = int(self.request.body)
        if value >= 0 and value <= 100:
            evaluation.mark = value
            evaluation.save()
        return response.Response(status=200)
