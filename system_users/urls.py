from django.urls import path, include
from system_users.views import (
    RegisterUserView, RetriveUserProfileView, ActivateAccountView, ChangePasswordView, UpdateProfileView,
    InviteMemberView, VerifyInviteView, RegisterInvitedMember, ResendInviteView, ListInvitedMembers, ListCompanyUsersView,
    UpdateCompanyDetaisView, ResendEmailVerificationView, ListCompaniesView, SuperUserInviteView, ResendSuperUserInvite, RegisterSuperAdminView, ListInvitedSuperAdminView
    )

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('retrive-profile/', RetriveUserProfileView.as_view()),
    path('activate-account/', ActivateAccountView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('update-profile/', UpdateProfileView.as_view()),
    path('invite-member/', InviteMemberView.as_view()),
    path('verify-invite/', VerifyInviteView.as_view()),
    path('register-invited-member/', RegisterInvitedMember.as_view()),
    path('resend-invite/', ResendInviteView.as_view()),
    path('list-invited-members/', ListInvitedMembers.as_view()),
    path('list-company-members/', ListCompanyUsersView.as_view()),
    path('update-company-details/', UpdateCompanyDetaisView.as_view()),
    path('resend-email-verification/', ResendEmailVerificationView.as_view()),
    path('list-companies/', ListCompaniesView.as_view()),
    path('invite-super-user/', SuperUserInviteView.as_view()),
    path('resend-super-user-invite/', ResendSuperUserInvite.as_view()),
    path('register-invited-super-admin/', RegisterSuperAdminView.as_view()),
    path('list-invited-super-admins/', ListInvitedSuperAdminView.as_view())
    ]