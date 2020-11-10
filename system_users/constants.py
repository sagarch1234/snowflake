#UI Host
UI_HOST = 'https://calm-meadow-01cfdeb10.azurestaticapps.net'

#login Page 
LOGIN_URL = UI_HOST

#forgot password page
FORGOT_PASSWORD_URL = UI_HOST+'/validate-token?token='

#member invite page
INVITE_MEMBER_URL = UI_HOST+'/verify-invite?token='

#super admin invite page
INVITE_SUPER_ADMIN = UI_HOST+'/verify-super-admin-invite?token='

#email subjects 
FORGOT_PASSWORD_SUBJECT = 'OTP to reset your password.'
ACCOUNT_PASSWORD_UPDATED = 'Your account password has been changed.'
ACCOUNT_ACTIVATED = 'Account activated.'
EMAIL_VERIFICATION = 'Verify your email to activate your account.'
INVITE_MEMBER = 'You have been invited to join Snowflake Optimizer.'
INVITE_SUPER_USER = 'You have been invited to join Snowflake Optimizer as a Super Admin.'


#user group
ORGANISATION_MEMBER = 'Organisation Member'
SUPER_ADMIN = 'Super Admin'
ORGANISATION_ADMIN = 'Organisation Admin'

#email templates