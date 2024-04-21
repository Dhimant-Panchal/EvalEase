from django.contrib import admin

from .models import (
    Module,
    Assignment,
    AcademicProfile,
    StudentProfile,
    Submission,
    ConvenerProfile,
    Evaluation,
)

# Register your models here.

admin.site.register(Module)
admin.site.register(Assignment)
admin.site.register(StudentProfile)
admin.site.register(Submission)
admin.site.register(AcademicProfile)
admin.site.register(ConvenerProfile)
admin.site.register(Evaluation)
