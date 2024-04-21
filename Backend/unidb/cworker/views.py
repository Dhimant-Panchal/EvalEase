from rest_framework import views, response, authentication, permissions


class UserProfileTypeView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        if hasattr(request.user, "studentprofile"):
            return response.Response("student")
        elif hasattr(request.user, "academicprofile"):
            return response.Response("academic")
        elif hasattr(request.user, "convenerprofile"):
            return response.Response("convener")


class UserNameView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        return response.Response(user.first_name + " " + user.last_name)
