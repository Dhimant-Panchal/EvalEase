from rest_framework import response, views
from itertools import islice

from .models import Keyword
from .serializers import KeywordSearchSerializer


class KeywordSearchView(views.APIView):
    def get(self, request, query: str):
        captured = Keyword.objects.filter(text__icontains=query)
        return response.Response(islice(map(lambda o: o.text, captured), 8))
