from django.urls import path, include

from snowflake_connector.views import(
    AddInstanceView
)


urlpatterns = [
    path('add-instance/', AddInstanceView.as_view())
]