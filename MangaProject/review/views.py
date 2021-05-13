from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Review, Reply
from .serializers import ReplySerializer, ReviewSerializer, ReplynReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]

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

