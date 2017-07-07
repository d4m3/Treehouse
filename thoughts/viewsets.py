from rest_framework import viewsets

from . import serializers

# ViewSets define the view behavior.
class ThoughtViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ThoughtSerializer

    def get_queryset(self):
        return self.request.user.thoughts.all()