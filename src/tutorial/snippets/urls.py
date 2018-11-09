from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# region Dạng Django Rest Framework hỗ trợ cho cbv
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),  
# ]
# endregion

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# urlpatterns = [
#     path('', views.api_root),
#     path(
#         'snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list',
#     ),
#     path(
#         'snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'
#     ),
#     path(
#         'snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'
#     ),
#     path(
#         'users/',
#         views.UserList.as_view(),
#         name='user-list'
#     ),
#     path(
#         'users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail'
#     ),
# ]

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
