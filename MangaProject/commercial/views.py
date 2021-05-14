from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Advertising
from .serializers import AdvertisingSerializer, AdvertisingFullSerializer

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
        advs = Advertising.objects.get(id=pk)
    except Advertising.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = AdvertisingFullSerializer(advs)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        advs.delete()
        return Response({'deleted': True})
permission_classes = (AllowAny,)