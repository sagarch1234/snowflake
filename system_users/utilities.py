'''
Python imports.
'''
import random
import string

from rest_framework import status


def generate_password():

    '''
    This method is to generate password which has at least one lowercase, uppercase, digit and special character.
    '''
    
    randomSource = string.ascii_letters + string.digits + string.punctuation
   
    
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(3):
        
        password += random.choice(randomSource) 
    
    passwordList = list(password)
    
    random.SystemRandom().shuffle(passwordList)
    
    password = ''.join(passwordList)

    return password


def generate_otp():
    
    '''
    This method will generate 4 digit random number.
    '''

    otp = random.randint(1111, 9999)

    return otp

        
def verify_otp_exist(user_id):

    from .models import EmailVerificationOtp

    try:

        generated_otp = EmailVerificationOtp.objects.get(user=user_id)

        return {
            "message" : "OTP exist.",
            "otp" : generated_otp.otp,
            "user": generated_otp.user.id,
            "status" : status.HTTP_302_FOUND
        }

    except EmailVerificationOtp.DoesNotExist:

        return {
            "message" : "OTP was not generated for the provicded user.",
            "status" : status.HTTP_404_NOT_FOUND
        }

def store_otp(otp, user_instance):

    from .models import EmailVerificationOtp, User

    otp = generate_otp()
    
    store_otp = EmailVerificationOtp(user=user_instance, otp=otp)

    otp_instance = store_otp.save()

    return otp