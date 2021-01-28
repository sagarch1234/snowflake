from snowflake_instances.models import Instances
import status


def get_instance(instance_id):
    '''
    This method will get the customer's snowflake instance.
    '''
    try:
        
        sf_instance = Instances.objects.get(id=instance_id)
        
    except Exception as identifier:

        print(identifier)

        return status.HTTP_404_NOT_FOUND
    
    return sf_instance

def get
    