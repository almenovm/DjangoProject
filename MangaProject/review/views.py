from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Review, Reply
from .serializers import ReplySerializer, ReviewSerializer, ReplynReviewSerializer

import logging

logger = logging.getLogger(__name__)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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

    # @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    # def create_review(self, request):
    #     serializer = ReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response('OK')
    #     return Response(serializer.errors)


class ReplyViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]
#
class ReplynReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Reply.objects.all()
    serializer_class = ReplynReviewSerializer

