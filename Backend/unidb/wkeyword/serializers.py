from rest_framework import serializers

from .models import Keyword


class KeywordSearchSerializer(serializers.ModelSerializer):
    uses = serializers.SerializerMethodField()

    class Meta:
        model = Keyword
        fields = ["id", "text", "uses"]

    def get_uses(self, obj):
        return obj.submission_set.count()
