from django.urls import path, include

from snowflake_instances.views import(
    AddInstanceView, ListInstancesView, UpdateInstanceview, ReconnectAllInstancesView, ReconnectInstanceView, RemoveInstanceView
)


urlpatterns = [
    path('add-instance/', AddInstanceView.as_view()),
    path('list-instances/', ListInstancesView.as_view()),
    path('update-instance/', UpdateInstanceview.as_view()),
    path('reconnect-all-instances/', ReconnectAllInstancesView.as_view()),
    path('reconnect-instance/', ReconnectInstanceView.as_view()),
    path('delete-instance/', RemoveInstanceView.as_view()),
]