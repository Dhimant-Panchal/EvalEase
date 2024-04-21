from django.db import models
from django.contrib.auth.models import User
from unidb.wkeyword.models import Keyword


class Module(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=30)


class Assignment(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name="assignments"
    )
    title = models.CharField(max_length=30)
    due_date = models.DateTimeField()


class StudentProfile(models.Model):
    modules = models.ManyToManyField(Module)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    urn = models.IntegerField(unique=True)


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    creator = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("assignment", "creator")


class AcademicProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Keyword)


class ConvenerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module)


class Evaluation(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    marker = models.ForeignKey(AcademicProfile, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("submission", "marker")
