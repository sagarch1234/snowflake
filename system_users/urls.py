from django.urls import path, include
from system_users.views import RegisterUserView, RetriveUserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('retrive-profile/', RetriveUserProfileView.as_view())
       
]