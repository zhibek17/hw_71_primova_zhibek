from rest_framework import serializers
from webapp.models import Publication, Like


class PublicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'description', 'author')


class LikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'publication')
