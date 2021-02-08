from django.db import models

from system_users.models import BaseModel, User
from snowflake_instances.models import Instances


class AuditStatus(models.Model):
    '''
    This model has the list of all the status an Audit can have.
    '''
    status = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):

        return 'Audit status Object ({})'.format(self.id)


class OneQueryRules(BaseModel):
    '''
    This model will store the list of all the rules created by super admin.
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
    The article links related to the rules created by super admin will be stored here.
    '''
    one_query_rule = models.ForeignKey(OneQueryRules, related_name = 'one_query_rule_related_articles', on_delete=models.CASCADE, blank=False)
    article_link = models.TextField(blank=False, null=False)

    def __str__(self):

        return 'One Query Rule Articles Object ({})'.format(self.id)


class IgnoreRules(BaseModel):
    '''
    This models stores the list of rules which should be ignored in audits for the specific instances.
    This data in this model is added by Organisation member or Organisation admin.
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
    Each audits registered by the user will be stored here.
    '''
    instance = models.ForeignKey(Instances, on_delete=models.CASCADE, blank=False)
    status = models.ForeignKey(AuditStatus, on_delete=models.CASCADE, blank=False)
    issue = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):

        return 'Audits Object ({})'.format(self.id)


class DoNotNotifyUsers(BaseModel):
    '''
    This models stores the list of users which should be ignored in audits notification for the specific instances.
    '''
    instance = models.ForeignKey(Instances, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = (('instance', 'user'),)

    def __str__(self):

        return 'Do Not Notify Users Object ({})'.format(self.id)


class ApplicableRule(BaseModel):
    '''
    This model stores the list of rules which were considered during the execution of Audits.
    '''
    audit = models.ForeignKey(Audits, on_delete=models.CASCADE, blank=False)
    rule_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    rule_description = models.TextField(blank=True, null=True)
    rule_evaluation_query = models.TextField(blank=False, null=False)
    rule_evaluation_equation = models.TextField(blank=False, null=False)
    failed_if = models.BooleanField(blank=False, null=False)
    rule_recommendation = models.TextField(blank=False, null=False)
    rule_dataset_query = models.TextField(blank=False, null=False)

    def __str__(self):

        return 'Applicable Rules Object ({})'.format(self.id)


class ApplicableRuleArticles(BaseModel):
    '''
    This model stores the list of articles related to the applicable rules.
    '''
    applicable_rule = models.ForeignKey(ApplicableRule, related_name = 'applicable_rule_related_articles', on_delete=models.CASCADE, blank=False)
    article_link = models.TextField(blank=False, null=False)

    def __str__(self):

        return 'Applicable Rule Articles Object ({})'.format(self.id)


class AuditsResults(BaseModel):
    '''
    This model will store the results of Audits.
    '''
    audit = models.ForeignKey(Audits, on_delete=models.CASCADE, blank=False)
    applicable_rule = models.ForeignKey(ApplicableRule, on_delete=models.CASCADE, blank=False)
    recommendation = models.TextField(blank=True, null=True)
    dataset = models.TextField(blank=True, null=True)

    def __str__(self):

        return 'Audits Results Object ({})'.format(self.id)
    

class AuditRecommendedArticles(BaseModel):
    '''
    This model will store the links of articles suggested by audits.
    '''
    audit_result = models.ForeignKey(AuditsResults, related_name = 'audit_recommended_article', on_delete=models.CASCADE, blank=False)
    article_links = models.TextField(blank=True, null=True)

    def __str__(self):

        return 'Audit Recommended Articles Object ({})'.format(self.id)