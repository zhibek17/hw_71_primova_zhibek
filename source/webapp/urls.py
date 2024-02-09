from django.urls import path
from .views.publication_views import HomeView, PublicationCreateView, PublicationLikeView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('publications/create/', PublicationCreateView.as_view(), name='publication_create'),
    path('publications/like/<int:pk>/', PublicationLikeView.as_view(), name='publication_like')
]