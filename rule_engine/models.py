from django.db import models

from system_users.models import BaseModel


class OneQueryRules(BaseModel):
    '''
    This model will store the list of all the rules created in each templates.
    '''
    rule_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    rule_description = models.TextField(blank=True, null=True)

    rule_evaluation_query = models.TextField(blank=False, null=False)
    
    rule_evaluation_equation = models.TextField(blank=False, null=False)
    failed_if = models.BooleanField(blank=False, null=False)

    rule_recommendation = models.TextField(blank=False, null=False)
    rule_dataset_query = models.TextField(blank=False, null=False)

    is_enabled = models.BooleanField(default=True, blank=False, null=False)


class OneQueryRuleArticles(BaseModel):
    '''
    '''
    one_query_rule = models.ForeignKey(OneQueryRules, related_name = 'one_query_rule_related_articles', on_delete=models.CASCADE, blank=False)
    article_link = models.TextField(blank=False, null=False)