from rest_framework import serializers

from unidb.cworker.models import (
    Assignment,
    Submission,
    Evaluation,
    AcademicProfile,
    Keyword,
)


class ConvenerAssignmentSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField(read_only=True, slug_field="code")
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = serializers.ALL_FIELDS

    def get_user_count(self, obj):
        return obj.module.studentprofile_set.count()


class ConvenerSubmissionSerializer(serializers.ModelSerializer):
    assignment = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    created_at = serializers.ReadOnlyField()
    keywords = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="text", queryset=Keyword.objects.all()
    )

    marker_count = serializers.SerializerMethodField()
    urn = serializers.SerializerMethodField()
    returned_marks = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = [
            "id",
            "assignment",
            "creator",
            "created_at",
            "marker_count",
            "urn",
            "keywords",
            "returned_marks",
        ]

    def get_marker_count(self, obj):
        return obj.evaluation_set.count()
    
    def get_returned_marks(self, obj):
        count = 0
        for o in obj.evaluation_set.all():
            if o.mark: count += 1
        return count

    def get_urn(self, obj):
        return obj.creator.urn


class ConvenerEvaluationSerializer(serializers.ModelSerializer):
    mark = serializers.ReadOnlyField()
    submission = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=Submission.objects.all()
    )
    marker = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=AcademicProfile.objects.all()
    )
    module = serializers.SerializerMethodField()
    urn  = serializers.SerializerMethodField()
    assignment_title = serializers.SerializerMethodField()

    class Meta:
        model = Evaluation
        fields = serializers.ALL_FIELDS

    def get_module(self, obj):
        return obj.submission.assignment.module.code
    
    def get_urn(self, obj):
        return obj.submission.creator.urn

    def get_assignment_title(self, obj):
        return obj.submission.assignment.title

    # def validate(self, attrs):
    #     return attrs.assignment.module in attrs.marker.module_set
