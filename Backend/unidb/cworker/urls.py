from django.urls import include, path
from rest_framework import routers

from .views import UserProfileTypeView, UserNameView

urlpatterns = [
    path(
        "me/profiletype",
        UserProfileTypeView.as_view(),
    ),
    path(
        "me/name",
        UserNameView.as_view(),
    ),
]
