"""Serializers for snippetsHy."""
from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight",
        format="html",
    )

    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "title", "code", "linenos",
                  "language", "style", "owner"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Since snippets is a relationship defined on the Snippet model, not the
    # User model, we need to explicitly add it for it to get serialized
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="snippet-detail",
        read_only=True,
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
