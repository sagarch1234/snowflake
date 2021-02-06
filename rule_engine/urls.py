from django.urls import path, include

from rule_engine.views import ( 
CreateOneQueryRuleView, ListOneQueryRuleView, EnableDisableOneQueryRuleView, AddRuleToIgnoreListView,
RemoveRuleFromIgnoreListView, RunAuditView, ListAuditsView, ListAuditResultsView, DoNotNotifyUsersView, 
UpdateRuleView, RemoveDoNotNotifyUsersView
)

urlpatterns = [
    path('create-one-query-rule/', CreateOneQueryRuleView.as_view()),
    path('list-one-query-rule/', ListOneQueryRuleView.as_view()),
    path('enable-disable-one-query-rule/', EnableDisableOneQueryRuleView.as_view()),
    path('add-rule-to-ignore-list/', AddRuleToIgnoreListView.as_view()),
    path('remove-rule-from-ignore-list/', RemoveRuleFromIgnoreListView.as_view()),
    path('run-audit/', RunAuditView.as_view()),
    path('list-audits/', ListAuditsView.as_view()),
    path('list-audit-results/', ListAuditResultsView.as_view()),
    path('do-not-notify-users/', DoNotNotifyUsersView.as_view()),
    path('update-rule/', UpdateRuleView.as_view()),
    path('remove-user-from-do-not-notify-list/', RemoveDoNotNotifyUsersView.as_view()),
]