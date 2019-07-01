from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, parsers, renderers, viewsets
from rest_framework.compat import coreapi, coreschema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import MyOwnToken as Token
from .serializers import AuthTokenSerializer, UserSerializer
from .utils import CustomMethod, DefaultMethod
from .utils import ActionMethod as action_schema

# Create your views here.
class TestView(View):
    def get(self, request, *args, **kwargs):
        # print(request.user)
        return JsonResponse({
            'result': 'TEST',
        })

@method_decorator(name='list', decorator=DefaultMethod.AccountListDecorator)
class TestViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @swagger_auto_schema(responses=CustomMethod.UserCreateResponse)
    @action_schema.user_test_schema
    @action(detail=False, methods=['get'])
    def test_test_test(self, request):
        return Response({
            "message": 'TEST',
            'user_id': 'TEST111',
        })

class HelloView(APIView):
    def get(self, request):
        # print(request.user)
        print(request.auth.user)
        content = {'message': 'Hello, World!'}
        return Response(content)


class Hello2View(APIView):
    def get(self, request):
        # print(request.user)
        print(request.auth.user)
        content = {'message': 'Hello, World!'}
        return Response(content)

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if created is False:
            token.openstack_cache = 'TESTA'
            token.expired = timezone.now()
            token.save()
        else:
            token.openstack_cache = 'TESTB'
            token.expired = timezone.now()
            token.save()
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()
