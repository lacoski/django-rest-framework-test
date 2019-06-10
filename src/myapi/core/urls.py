from django.urls import path
from core import views
from .views import obtain_auth_token, TestView


urlpatterns = [
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test_view/', TestView.as_view(), name='test_view'),
]
