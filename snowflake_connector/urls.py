from django.urls import path, include

from snowflake_connector.views import(
    AddInstanceView, ListInstancesView
)


urlpatterns = [
    path('add-instance/', AddInstanceView.as_view()),
    path('list-instances/', ListInstancesView.as_view())
]