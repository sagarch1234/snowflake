from django.urls import path, include

from snowflake_connector.views import(
    AddInstanceView, ListInstancesView, UpdateInstanceview, ReconnectAllInstances, ReconnectInstance
)


urlpatterns = [
    path('add-instance/', AddInstanceView.as_view()),
    path('list-instances/', ListInstancesView.as_view()),
    path('update-instance/', UpdateInstanceview.as_view()),
    path('reconnect-all-instances/', ReconnectAllInstances.as_view()),
    path('reconnect-instance/', ReconnectInstance.as_view())
]