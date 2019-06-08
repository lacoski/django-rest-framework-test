from rest_framework.authentication import TokenAuthentication
from core.models import MyOwnToken

class MyOwnTokenAuthentication(TokenAuthentication):
    model = MyOwnToken
