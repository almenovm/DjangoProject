from rest_framework import serializers
from .models import Review, Reply

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def validate_title(self, value):
        if '#' and '_' and '*' and '$' in value:
            raise serializers.ValidationError('invaild symbols, do not use # / _ % *')
        return value

class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = ('main_user', 'text', 'created_date')

class ReplynReviewSerializer(ReplySerializer):
    review = ReviewSerializer

    class Meta(ReplySerializer.Meta):
        fields = ReplySerializer.Meta.fields + ('review',)