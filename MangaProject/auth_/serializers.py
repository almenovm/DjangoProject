from rest_framework import serializers

from auth_.models import MainUser, Profile


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date',)

class ProfileFullSerializer(ProfileSerializer):
    user = MainUserSerializer

    class Meta(ProfileSerializer.Meta):
        fields = ProfileSerializer.Meta.fields + ('user',)
