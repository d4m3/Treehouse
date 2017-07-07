from django.contrib.auth.models import User

from rest_framework import viewsets

from . import serializers


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
