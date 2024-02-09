from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView, UserChangeView, UserPasswordChangeView, UserDetailView, UserSearchView, \
    UserSubscriptionView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='user_create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='user_change'),
    path('<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('users/search/', UserSearchView.as_view(), name='user_search'),
    path('users/subscription/<int:pk>/', UserSubscriptionView.as_view(), name='user_subscription')

]