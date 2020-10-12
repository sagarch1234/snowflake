from django.urls import path, include
from system_users.views import RegisterUserView, RetriveUserProfileView, ActivateAccountView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('retrive-profile/', RetriveUserProfileView.as_view()),
    path('activate-account/', ActivateAccountView.as_view()),
    path('change-password/', ChangePasswordView.as_view())
]