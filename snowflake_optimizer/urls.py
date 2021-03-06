"""snowflake_optimizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenRefreshView

from system_users.views import TokenObtainPairView

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snowflake Optimizer's API",
      default_version='v1',
      description="Base URL configuration for Snowflake Optimizer.",
      contact=openapi.Contact(email="SnowflakeOptimizer@emphasistech.net"),
      license=openapi.License(name="BSD License"),
   ),
   url='https://calm-meadow-01cfdeb10.azurestaticapps.net/',
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    #redirect user to the API documentation.
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    #login and refresh token using simple-jwt package
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #forgot password implemented using django_rest_passwordreset package 
    path('api/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    #redirect to system user's app where user can change password, view profile, invite users, updated profile and many more profile related operations.
    path('api/users/', include('system_users.urls')),

    #redirect to advertisement app where user can add advertisement, update, delete and many more advertisement related opertaions can be performed.
    path('api/advertisement/', include('advertisement.urls')),

    #redirect to snowflake-instances app where user can connect snowflake instances with our system and can also perform operations like test connection, update connection etc.
    path('api/snowflake-instances/', include('snowflake_instances.urls')),

    path('api/rule-engine/', include('rule_engine.urls'))

]
