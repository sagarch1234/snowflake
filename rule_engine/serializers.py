from rest_framework import serializers
from django.db import transaction

from rule_engine.models import OneQueryRules, OneQueryRuleArticles, IgnoreRules, Audits, AuditsResults, DoNotNotifyUsers, ApplicableRule, ApplicableRuleArticles
from snowflake_instances.models import Instances


class ApplicableRuleArticlesSerializer(serializers.ModelSerializer):
    '''
    ''' 
    class Meta:
        model = ApplicableRuleArticles
        fields = ['id', 'applicable_rule', 'article_link']
        extra_kwargs = {
            'applicable_rule' : {
                'required' : False
            }
        }


class ApplicableRuleSerializer(serializers.ModelSerializer):
    '''
    '''
    one_query_rule_related_articles = ApplicableRuleArticlesSerializer(many=True)
    class Meta:
        
        model = ApplicableRule
        fields = ['id', 'audit', 'rule_name', 'rule_description', 'rule_evaluation_query', 'rule_evaluation_equation', 'failed_if', 'rule_recommendation', 'rule_dataset_query', 'one_query_rule_related_articles']
    
    def create(self, validated_data):

        applicable_article = validated_data.pop('one_query_rule_related_articles')

        obj = ApplicableRule.objects.create(**validated_data)

        for each in applicable_article:

            article_obj = ApplicableRuleArticles.objects.create(applicable_rule=obj, article_link=each['article_link'])
        
        return obj

        


class DoNotNotifyUsersSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        model = DoNotNotifyUsers
        fields = ['id', 'instance', 'user']
        extra_kwargs = {
            'instance' : {
                'required' : True,
                'allow_null' : False,
            },
            'user' : {
                'required' : True,
                'allow_null' : False,
            }
        }


class AuditsResultsSerializer(serializers.ModelSerializer):
    '''
    '''

    class Meta:
        model = AuditsResults
        fields = ['id', 'recommendation', 'dataset']
        extra_kwargs = {
            'recommendation' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'dataset' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            }
        }


class AuditsSerializer(serializers.ModelSerializer):
    '''
    '''

    class Meta:
        model = Audits
        fields = ['id', 'status', 'issue', 'user']
        extra_kwargs = {
            'status' : {
                'required' : True,
                'allow_null' : False,
            },
            'user' : {
                'required' : True,
                'allow_null' : False,
            }
        }


class IgnoreRulesSerializer(serializers.ModelSerializer):
    '''
    '''

    class Meta:

        model = IgnoreRules
        fields = ['id', 'one_query_rule', 'instance', 'user']
        extra_kwargs = {
            'id' : {
                'required' : False,
                'read_only' : True,
            },
            'one_query_rule' : {
                'required' : True,
                'allow_null' : False,
            },
            'instance' : {
                'required' : True,
                'allow_null' : False,
            },
            'user' : {
                'required' : False,
                'allow_null' : False,
            }
        }


class OneQueryRuleArticlesSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:

        model = OneQueryRuleArticles
        fields = ['id', 'one_query_rule', 'article_link']
        extra_kwargs = {
            'one_query_rule' : {
                'required' : False,
                'allow_null' : False,
                'read_only': True
            },
            'article_link' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            }
        }


class OneQueryRuleSerializer(serializers.ModelSerializer):
    '''
    '''
    one_query_rule_related_articles = OneQueryRuleArticlesSerializer(many=True)

    class Meta:
        
        model = OneQueryRules
        fields = ['id', 'rule_name', 'rule_description', 'rule_evaluation_query', 'rule_evaluation_equation', 'failed_if', 'rule_recommendation', 'rule_dataset_query', 'is_enabled', 'one_query_rule_related_articles']
        extra_kwargs = {
            'rule_name' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'rule_description' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'rule_evaluation_query' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'rule_evaluation_equation' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'failed_if' : {
                'required' : True,
                'allow_null' : False,
            },
            'rule_recommendation' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'rule_dataset_query' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'is_enabled' : {
                'required' : True,
                'allow_null' : False,
            },
            'one_query_rule_related_articles' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            }
        }

    @transaction.atomic
    def create(self, validated_data):

        articles = validated_data.pop('one_query_rule_related_articles')

        rule = OneQueryRules.objects.create(**validated_data)

        for article in articles:

            article_id = OneQueryRuleArticles.objects.create(one_query_rule=rule, **article)
        
        return rule
        
    @transaction.atomic
    def update(self, instance, validated_data, articles=None):

        articles = self.context['articles']

        if not articles is None:

            for article in articles:

                try:

                    article_instance = OneQueryRuleArticles.objects.get(id=article['id'])
                
                except Exception as identifier:

                    print(str(identifier))
                
                article_instance.article_link = article['article_link']

                article_instance.save()

        instance.rule_name = validated_data.get('rule_name', instance.rule_name)
        instance.rule_description = validated_data.get('rule_description', instance.rule_description)
        instance.rule_evaluation_query = validated_data.get('rule_evaluation_query', instance.rule_evaluation_query)
        instance.rule_evaluation_equation = validated_data.get('rule_evaluation_equation', instance.rule_evaluation_equation)
        instance.failed_if = validated_data.get('failed_if', instance.failed_if)
        instance.rule_recommendation = validated_data.get('rule_recommendation', instance.rule_recommendation)
        instance.rule_dataset_query = validated_data.get('rule_dataset_query', instance.rule_dataset_query)
        instance.is_enabled = validated_data.get('is_enabled', instance.is_enabled)

        instance.save()
        
        return instance

