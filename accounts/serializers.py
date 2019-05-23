from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    """ Serializer """

    class Meta(object):
        """ Meta """
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(HyperlinkedModelSerializer):
    """ Serializer """

    class Meta(object):
        """ Meta """
        model = Group
        fields = ('url', 'name')
