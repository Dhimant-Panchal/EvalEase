from rest_framework import serializers

from unidb.wkeyword.models import Keyword
from unidb.cworker.models import Submission, AcademicProfile


class AcademicProfileSerializer(serializers.ModelSerializer):
    interests = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="text", queryset=Keyword.objects.all()
    )
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = ["id", "interests", "full_name"]

    def get_full_name(self, obj):
        user = obj.user
        return user.first_name + " " + user.last_name