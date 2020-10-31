from django.urls import path, include

from snowflake_connector.views import(
    AddInstanceView, ListInstancesView, UpdateInstanceview
)


urlpatterns = [
    path('add-instance/', AddInstanceView.as_view()),
    path('list-instances/', ListInstancesView.as_view()),
    path('update-instance/', UpdateInstanceview.as_view())
]