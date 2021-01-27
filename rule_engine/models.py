from django.db import models

from system_users.models import BaseModel, User
from snowflake_instances.models import Instances


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

    def __str__(self):

        return 'One Query Rules Object ({})'.format(self.id)



class OneQueryRuleArticles(BaseModel):
    '''
    '''
    one_query_rule = models.ForeignKey(OneQueryRules, related_name = 'one_query_rule_related_articles', on_delete=models.CASCADE, blank=False)
    article_link = models.TextField(blank=False, null=False)

    def __str__(self):

        return 'One Query Rule Articles Object ({})'.format(self.id)


class IgnoreRules(BaseModel):
    '''
    '''
    one_query_rule = models.ForeignKey(OneQueryRules, on_delete=models.CASCADE, blank=False)
    instance = models.ForeignKey(Instances, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = (('one_query_rule', 'instance'),)


    def __str__(self):

        return 'Ignored Rule Object ({})'.format(self.id)


class Audits(BaseModel):
    '''
    '''
    instance = models.ForeignKey(Instances, on_delete=models.CASCADE, blank=False)
    status = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):

        return 'Audits Object ({})'.format(self.id)


class AuditsResults(BaseModel):
    '''
    '''
    audit = models.ForeignKey(Audits, on_delete=models.CASCADE, blank=False)
    one_query_rule = models.ForeignKey(OneQueryRules, on_delete=models.CASCADE, blank=False)
    recommendation = models.TextField(blank=True, null=True)
    dataset = models.TextField(blank=True, null=True)

    def __str__(self):

        return 'Audits Results Object ({})'.format(self.id)


class DoNotNotifyUsers(BaseModel):
    '''
    '''
    audit = models.ForeignKey(Audits, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = (('audit', 'user'),)

    def __str__(self):

        return 'Do Not Notify Users Object ({})'.format(self.id)


class AuditStatus(models.Model):
    '''
    '''
    status = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):

        return 'Audit status Object ({})'.format(self.id)