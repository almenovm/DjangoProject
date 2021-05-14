from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileFullSerializer

from .models import Profile, MainUser
import logging

logger = logging.getLogger(__name__)
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileFullSerializer

    def get_permissions(self):
        logger.debug('get permissions')
        logger.info('get permissions')
        logger.warning('get permissions')
        logger.error('get permissions')
        logger.critical('get permissions')

        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]