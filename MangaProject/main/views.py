from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from main.models import Manga, Ranobe, Publisher, SemilarManga, SemilarRanobe
from main.serializers import MangaSerializer, RanobeSerializer, PublisherSerializer, SemilarMangaSerializer, \
    SemilarRanobeSerializer, MangaFullSerializer, RanobeFullSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class MangaViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,)
    search_fields = ('name', 'genre',)

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


class RanobeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Ranobe.objects.all()
    serializer_class = RanobeSerializer

class MangaFullViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Manga.objects.all()
    serializer_class = MangaFullSerializer

class RanobeFullViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Ranobe.objects.all()
    serializer_class = RanobeFullSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,)

    search_fields = ('name', 'genre', 'num_pages',)

class PublisherListAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)

class PublisherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)

class SemilarMangaListAPIView(generics.ListCreateAPIView):
    queryset = SemilarManga.objects.all()
    serializer_class = SemilarMangaSerializer
    permission_classes = (AllowAny,)

class SemilarMangaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemilarManga.objects.all()
    serializer_class = SemilarMangaSerializer
    permission_classes = (AllowAny,)

class SemilarRanobeListAPIView(generics.ListCreateAPIView):
    queryset = SemilarRanobe.objects.all()
    serializer_class = SemilarRanobeSerializer
    permission_classes = (AllowAny,)


class SemilarRanobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SemilarRanobe.objects.all()
    serializer_class = SemilarRanobeSerializer
    # serializer_class.is_valid(raise_exception=True)
    permission_classes = (AllowAny,)

