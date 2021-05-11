from rest_framework import serializers
from main.models import Manga, Ranobe


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranobe
        fields = '__all__'
