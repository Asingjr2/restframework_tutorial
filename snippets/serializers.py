"""
    Serializer class handles base logic and data element transfers for url requests from database.  Also used in angular
"""

from django.contrib.auth.models import User

from rest_framework import serializers 

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


#  Below classes use ModelSerializer vice HyperLinkedModelSerializer
# Differnce is functionality and information returned.
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "linenos", "language", "style", "owner")

# PrimaryKeyRelated field changes when class is Hyperlinked.....
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset= Snippet.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "snippets")


