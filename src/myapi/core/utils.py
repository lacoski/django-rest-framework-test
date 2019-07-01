from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class DefaultMethod(object):
    AccountListDecorator = swagger_auto_schema(
        operation_description="List User 123"
    )

class ActionMethod(object):
    user_test_schema = swagger_auto_schema(
        operation_description="List User 123",
        responses={
            "201": openapi.Response(
                description="Created",
                examples={
                    'application/json': {
                        "message": "string",
                        'user_id': "string",
                    }
                })
        }
    )

class CustomMethod(object):
    UserCreateResponse = {
        "201": openapi.Response(
            description="Created",
            examples={
                'application/json': {
                    "message": "string",
                    'user_id': "string",
                }
            })
    }