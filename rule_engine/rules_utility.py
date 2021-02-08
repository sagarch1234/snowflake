from snowflake_instances.models import Instances

from snowflake.instance_connector.connection import SnowflakeConnector

from rule_engine.models import Audits, AuditStatus, OneQueryRules, IgnoreRules, DoNotNotifyUsers, ApplicableRule, AuditRecommendedArticles
from rule_engine.serializers import OneQueryRuleSerializer, ApplicableRuleSerializer

from snowflake_instances.models import Instances

from system_users.models import User

from rest_framework.parsers import JSONParser

from django.db import transaction

import status, json


def get_instance(instance_id):
    '''
    This method will get the customer's snowflake instance.
    '''
    try:
        
        sf_instance = Instances.objects.get(id=instance_id)
        
    except Exception as identifier:

        return status.HTTP_404_NOT_FOUND
    
    return sf_instance


def connect_to_customer_sf_instance(user, password, account, audit_id):
    '''
    This method will try to connect to customer's snowflake instance. if the connection is successful it will return the connection object or else it will return the error object.
    In case of unsuccessful connection this method will update the status of audit to connection error and it will add the issue to the audit's table for this audit.
    In case of successful connection this method will update the status of audit to connected.
    '''
    
    snowflake_connector = SnowflakeConnector(user=user, password=password, account=account, role='ACCOUNTADMIN')
    connection = snowflake_connector.connect_snowflake_instance()

    audit_status = AuditStatus.objects.all()
    audit = Audits.objects.get(id=audit_id)
    
    if connection['status'] == status.HTTP_400_BAD_REQUEST:
        
        # update the status of the audit and add the connection[error] in issue.
        
        audit.status = audit_status[4]
        audit.issue = connection['error']
        audit.save()

    # update the status of the audit if the connection successful.

    audit.status = audit_status[1]
    audit.save()

    return connection


def prepare_rule_set(instance):
    '''
    This method will prepare the set of rules which will be executed for that instance.
    This method need instance_id.
    It will return the list of intance_id's or instance objects.
    '''

    all_rules = OneQueryRules.objects.filter(is_enabled=True)
    ignore_rule = IgnoreRules.objects.filter(instance=instance)

    final_all_rule = []
    final_ignore_rule = []

    for rule in all_rules:

        rule_id = rule.id

        final_all_rule.append(rule_id)

    
    for rule in ignore_rule:
        
        rule_id = rule.one_query_rule.id

        final_ignore_rule.append(rule_id)
 
    return list(set(final_all_rule).symmetric_difference(set(final_ignore_rule)))


def mail_to_users(instance_id, company_id):
    '''
    '''
    all_users = User.objects.filter(company = company_id, is_active=True)
    ignore_user = DoNotNotifyUsers.objects.filter(instance = instance_id)

    final_all_users = []
    final_ignore_users =[]

    for user in all_users:

        user_email = user.email
        final_all_users.append(user_email)
    
    for obj in ignore_user:

        user_email = obj.user.email
        final_ignore_users.append(user_email)

    return list(set(final_all_users).symmetric_difference(set(final_ignore_users)))


@transaction.atomic
def store_applicable_rules_and_articles(applicable_rules, audit_id):
    '''
    This method will store the applicable rules for the audit in the table AppliedRules.
    Method prepare rule set will provide the list of all the applicable rules ids.
    '''
    
    audit_object = Audits.objects.get(id=audit_id)

    #get the object of each rule
    rule_object = OneQueryRules.objects.filter(id__in=applicable_rules)

    #serialize rule object
    applicable_rules = OneQueryRuleSerializer(rule_object, many=True)

    rules_to_store = []

    for each_rule in applicable_rules.data:
        rule_to_json = json.dumps(each_rule)
        rule_to_json = json.loads(rule_to_json)
        rule_to_json['audit'] = audit_object
        rules_to_store.append(rule_to_json)
    
    rule_obj_list = []

    for each_rule in rules_to_store:
    
        rule_obj_list.append(ApplicableRule(audit = each_rule['audit'], rule_name = each_rule['rule_name'], rule_description = each_rule['rule_description'], rule_evaluation_query = each_rule['rule_evaluation_query'], rule_evaluation_equation= each_rule['rule_evaluation_equation'], failed_if= each_rule['failed_if'], rule_recommendation= each_rule['rule_recommendation'], rule_dataset_query= each_rule['rule_dataset_query']))

    rules_saved = ApplicableRule.objects.bulk_create(rule_obj_list)

    return rules_saved


def execute_appicable_rules(applicable_rules):
    '''
    [
        {
            "audit_id":,
            "applicable_rule":,
            "recommendation":""
            "dataset":""
            "audit_recommended_articles":{
                "audit_result":
                "article_link":
            }
        },
        {
            "audit_id":,
            "applicable_rule":,
            "recommendation":""
            "dataset":""
            "audit_recommended_articles":{
                "audit_result":
                "article_link":
            }
        }
    ]
    '''
    pass


def store_audit_results(audit_result):
    '''
    '''
    pass