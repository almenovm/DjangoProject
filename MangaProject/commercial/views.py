from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Advertising
from .serializers import AdvertisingSerializer, AdvertisingFullSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def advs_list(request):
    if request.method == 'GET':
       advs = Advertising.objects.all()
       serializer = AdvertisingSerializer(advs, many=True)
       return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
permission_classes = (AllowAny,)

@api_view(['GET', 'DELETE'])
def advs_detail(request, pk):
    try:
        advs = Advertising.objects.get(pk=pk)
    except Advertising.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = AdvertisingFullSerializer(advs)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'DELETE':
        advs.delete()
        logger.debug('deleted')
        logger.info('deleted')
        logger.warning('deleted')
        logger.error('deleted')
        logger.critical('deleted')
        return JsonResponse({'message': 'Advertising was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)