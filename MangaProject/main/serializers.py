from rest_framework import serializers
from main.models import Manga, Ranobe, Publisher, SemilarRanobe, SemilarManga


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = '__all__'


class RanobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranobe
        fields = '__all__'

class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()

    def create(self, validated_data):
        publisher = Publisher.objects.create(name=validated_data.get('name'), address=validated_data.get('address'), city=validated_data.get('city'), country=validated_data.get('country'))
        return publisher

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class SemilarMangaSerializer(serializers.Serializer):
    name = serializers.CharField()
    manga = serializers.PrimaryKeyRelatedField

    def create(self, validated_data):
        manga = SemilarManga.objects.create(name=validated_data.get('name'), manga=validated_data.get('manga'))
        return manga

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.manga = validated_data.get('manga', instance.manga)
        instance.save()
        return instance

class SemilarRanobeSerializer(serializers.Serializer):
    name = serializers.CharField()
    ranobe = serializers.PrimaryKeyRelatedField

    def create(self, validated_data):
        ranobe = SemilarManga.objects.create(name=validated_data.get('name'), ranobe=validated_data.get('ranobe'))
        return ranobe

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ranobe = validated_data.get('ranobe', instance.ranobe)
        instance.save()
        return instance
