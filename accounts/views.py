from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ModelViewSet):
    """ API endpoint allowing Users to be viewed and edited """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    """ API endpoint allowing Groups to be viewed and edited """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
