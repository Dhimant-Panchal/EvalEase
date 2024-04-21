"""
URL configuration for unidb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token

from unidb.cworker.urls import urlpatterns as cworker_urls
from unidb.wkeyword.urls import urlpatterns as wkeyword_urls
from unidb.student.urls import urlpatterns as student_urls
from unidb.academic.urls import urlpatterns as academic_urls
from unidb.convener.urls import urlpatterns as convener_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", obtain_auth_token),
    path("api/keyword/", include(wkeyword_urls)),
    path("api/student/", include(student_urls)),
    path("api/academic/", include(academic_urls)),
    path("api/convener/", include(convener_urls)),
    path("api/cworker/", include(cworker_urls)),
]
