from datetime import date


class AssociateData():

    def __init__(self, instance_id, user_id, event, company_id):
        self.instance_id = instance_id
        self.user_id = user_id
        self.event = event
        self.company_id = company_id
        self.date_run = date.today()
    
    def associate_data(self, dataframe):
        
        dataframe['instance_id'] = self.instance_id
        dataframe['user_id'] = self.user_id
        dataframe['event'] = self.event
        dataframe['company_id'] = self.company_id
        dataframe['date_run'] = self.date_run

        return dataframe