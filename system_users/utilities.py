'''
Python imports.
'''
import random
import string
import re


from rest_framework import status


def capitalize_name(input_name):
    """
    Method to capitalize first character of name.
    If '.' is present in string then first character of every list 
    element after splitting input string by '.'  is capitalized.
    This method should be called iff is_valid_name() returns True.
    Input : name (allowed)
    Output : Capitalized name
    """
    
    splitted_name = input_name.split('.')

    word_list = []
    
    for word in splitted_name:
    
        word_list.append(word[0].upper() + word[1:])
    
    return ('.'.join(word_list))


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
            "message" : "OTP was not generated for the provided user.",
            "status" : status.HTTP_404_NOT_FOUND
        }


def store_otp(otp, user_instance):

    from .models import EmailVerificationOtp, User

    otp = generate_otp()
    
    store_otp = EmailVerificationOtp(user=user_instance, otp=otp)

    otp_instance = store_otp.save()

    return otp

