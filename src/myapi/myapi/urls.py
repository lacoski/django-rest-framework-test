"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import rest_auth
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from core import views
# from rest_framework.authtoken.views import obtain_auth_token
from core.views import TestView, obtain_auth_token, Hello2View

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'users', views.TestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('test3/', include([
        path('hello1/', views.HelloView.as_view()),
        path('hello2/', views.Hello2View.as_view()),
    ])),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls