

#login Page 
LOGIN_URL = 'http://127.0.0.1:3000'

#forgot password page
FORGOT_PASSWORD_URL = 'http://127.0.0.1:3000/pages/validate-token?token='

#member invite page
INVITE_MEMBER_URL = 'http://127.0.0.1:3000/verify-invite?token='

#super admin invite page
INVITE_SUPER_ADMIN = 'http://127.0.0.1:3000/verify-super-admin-invite?token='

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