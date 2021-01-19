from django.urls import path, include

from rule_engine.views import CreateOneQueryRuleView, ListOneQueryRuleView, EnableDisableOneQueryRuleView

urlpatterns = [
    path('create-one-query-rule/', CreateOneQueryRuleView.as_view()),
    path('list-one-query-rule/', ListOneQueryRuleView.as_view()),
    path('enable-disable-one-query-rule/', EnableDisableOneQueryRuleView.as_view()),
]