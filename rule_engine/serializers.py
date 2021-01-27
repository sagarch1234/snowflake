from rest_framework import serializers
from django.db import transaction

from rule_engine.models import OneQueryRules, OneQueryRuleArticles, IgnoreRules, Audits, AuditsResults


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
        fields = ['id', 'status']
        extra_kwargs = {
            'status' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            }
        }


class IgnoreRulesSerializer(serializers.ModelSerializer):
    '''
    '''

    class Meta:

        model = IgnoreRules
        fields = ['id', 'one_query_rule', 'instance', 'user']
        extra_kwargs = {
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