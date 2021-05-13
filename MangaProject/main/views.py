from rest_framework import viewsets, generics
from main.models import Manga, Ranobe, Publisher, SemilarManga, SemilarRanobe
from main.serializers import MangaSerializer, RanobeSerializer, PublisherSerializer, SemilarMangaSerializer, SemilarRanobeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class MangaViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]


class RanobeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Ranobe.objects.all()
    serializer_class = RanobeSerializer

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
    permission_classes = (AllowAny,)