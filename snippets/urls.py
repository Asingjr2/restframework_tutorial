"""
    Urls file controls url requirements to see specific pages.  Can add suffic to declare type of request data explicitly.

    Individual urlpatterns for classbased views replaced with rest_framework viewset that allows access to more methods and has url patterns handled by the router class.
"""
from django.urls import path, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from . import views
from .views import SnippetViewSet, UserViewSet


# Django rest_framework router will handle url creation
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet)
router.register(r"users", views.UserViewSet)

# Adds additional response type from api
schema_view = get_schema_view(title="Pastebin API")

urlpatterns = [
    path("schema/", schema_view),
    path("", include(router.urls))
]

# Creating url links by attaching type to method type to a viewset function
snippet_list = SnippetViewSet.as_view({
    "get": "list", 
    "post": "create"
})

snippet_detail = SnippetViewSet.as_view({
    "get":"retrieve", 
    "put":"update", 
    "patch":"partial_update", 
    "detele": "destroy"
})
snippet_highlight = SnippetViewSet.as_view({
    "get":"hightlight"
}, renderer_classes = [renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    "get":"list"
})
user_detail = UserViewSet.as_view({
    "get":"retrieve"
})


# Standard urlviews...before replacement with viewsets
# urlpatterns = [
#     path("", views.api_root), 
#     path("snippets/", SnippetList.as_view(), name="snippet-list"), 
#     path("users/<int:id>/", UserDetail.as_view(), name="user-detail"),
#     path("snippets/<int:id>/", SnippetDetail.as_view(),name="snippet-detail"), 
#     path("snippets/<int:id>/highlight/", SnippetHighlight.as_view(), name="snippet-highlight"),
#     path("users/", views.UserList.as_view(), name="user-list"), 
# ]
