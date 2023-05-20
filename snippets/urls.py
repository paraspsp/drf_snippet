"""
Snippets URLs Configuration
"""

# django imports
from django.urls import path, include

# rest framework imports
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# snippets imports
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet


# binding viewsets to URL
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail =  SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'},
    renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # path('', views.api_root),
    # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),    
]

# urlpatterns = format_suffix_patterns(urlpatterns)