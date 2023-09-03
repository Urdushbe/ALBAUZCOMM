from django.urls import path
from .views import RegistrationView, UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('users/profile_update/<int:pk>/', UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('users/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]