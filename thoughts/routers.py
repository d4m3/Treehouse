from rest_framework import routers

from . import viewsets
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'thoughts', viewsets.ThoughtViewSet, base_name='thoughts')
