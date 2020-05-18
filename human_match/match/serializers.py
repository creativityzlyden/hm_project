from rest_framework import serializers

from .models import Match


class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def create(self, validated_data):
        return Match.objects.create(**validated_data)


class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
