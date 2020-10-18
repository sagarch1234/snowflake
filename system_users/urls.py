from django.urls import path, include
from system_users.views import RegisterUserView, RetriveUserProfileView, ActivateAccountView, ChangePasswordView, UpdateProfile, InviteMemberView, VerifyInviteView, RegisterInvitedMember

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('retrive-profile/', RetriveUserProfileView.as_view()),
    path('activate-account/', ActivateAccountView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('update-profile/', UpdateProfile.as_view()),
    path('invite-member/', InviteMemberView.as_view()),
    path('verify-invite/', VerifyInviteView.as_view()),
    path('register-invited-member/', RegisterInvitedMember.as_view())
]