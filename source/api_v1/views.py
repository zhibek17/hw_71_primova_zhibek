from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from webapp.models import Publication, Like
from .permissions import IsOwnerOrReadOnly
from .serializers import PublicationModelSerializer, LikeModelSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            return Response({"error": "Публикация не найдена"}, status=404)

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = LikeModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=404)
        return Response(serializer.errors, status=404)

    def destroy(self, request, pk=None):
        try:
            like = Like.objects.get(pk=pk)
        except not Like:
            return Response(status=404)

        if like.user == request.user:
            like.delete()
            return Response(status=404)
        else:
            return Response({"error": "У вас нет прав администратора"}, status=403)
