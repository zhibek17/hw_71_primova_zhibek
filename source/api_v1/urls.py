from django.urls import path, include
from rest_framework import routers
from .views import PublicationViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet, basename='publication')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
]
