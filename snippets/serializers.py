from rest_framework.serializers import ModelSerializer
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(ModelSerializer):
    """ Serializer """

    class Meta(object):
        """ Meta """
        model = Snippet
        fields = ('id', 'title', 'line_numbers', 'language', 'style')
