from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


from braces.views import LoginRequiredMixin
# Create your views here.


class UserViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    login_url = 'api-auth/'
    raise_exception = False
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    login_url = 'api-auth/'
    raise_exception = False
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
