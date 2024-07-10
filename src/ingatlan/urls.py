"""
URL configuration for ingatlan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from cases.api.urls import urlpatterns as case_url_patterns
from ingatlan.utils import MyAutocompleteJsonView
from user.api.urls import urlpatterns as user_url_patterns

api_urlpatterns = [

    path('files/', include(case_url_patterns)),
    path('user/', include(user_url_patterns)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Ingatlan API",
        default_version='v1',
        description="",
    ),
    url=settings.BASE_URL,
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[]
)

urlpatterns = [
    # path("__debug__/", include("debug_toolbar.urls")), # NOTE: turn this on , only on local
    path(
        f'{settings.PROJECT_NAME}/admin/'
        if settings.PROJECT_NAME
        else 'admin/',
        admin.site.urls
    ),
    path(
        f'{settings.PROJECT_NAME}/api/'
        if settings.PROJECT_NAME
        else 'api/',
        include(api_urlpatterns)
    ),
    # path(
    #     'silk/',
    #     include('silk.urls', namespace='silk')
    # ),
    # Swagger endpoints
    path(
        f'{settings.PROJECT_NAME}/swagger.json'
        if settings.PROJECT_NAME
        else 'swagger.json',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        f'{settings.PROJECT_NAME}/swagger/'
        if settings.PROJECT_NAME
        else 'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        f'{settings.PROJECT_NAME}/redoc/'
        if settings.PROJECT_NAME
        else 'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path(
        'autocomplete',
        MyAutocompleteJsonView.as_view(admin_site=admin.site),
        name='autocomplete'
    ),

]
