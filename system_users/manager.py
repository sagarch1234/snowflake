from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    """
    This is a User model's manager class.
    """
    
    def create_user(self, first_name, last_name, email, password, mobile_number=None, is_mobile_number_verified=None, company=None, is_email_varified=None, is_active=None):

        """
        This method will create a User object.
        """

        '''
        Check if the email field has the value and not empty.
        '''
        if not email:
            '''
            Raise an appropriate error if the email field is empty.
            '''
            raise ValueError("You need an email to create account")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name, 
            mobile_number = mobile_number, 
            password  = password, 
            company = company, 
            is_mobile_number_verified = is_mobile_number_verified,
            is_email_varified = is_email_varified,
            is_active = is_active
        )

        '''
        Encrypt password before storing.
        '''
        user.set_password(password)

        '''
        Save the object to the model.
        '''
        user.save(using = self._db)
        '''
        Return newly created object's string representation.
        '''
        
        return user

        