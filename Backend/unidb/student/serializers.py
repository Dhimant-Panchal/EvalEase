from rest_framework import serializers

from unidb.wkeyword.models import Keyword
from unidb.cworker.models import Submission


class StudentSubmissionSerializer(serializers.ModelSerializer):
    keywords = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="text", queryset=Keyword.objects.all()
    )

    class Meta:
        model = Submission
        fields = ["keywords"]
