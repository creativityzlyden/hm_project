from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Match
from .serializers import MatchListSerializer, MatchDetailSerializer
from rest_framework.pagination import PageNumberPagination


class MatchListView(generics.ListAPIView):
    """Вывод списка"""
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer
    pagination_class = PageNumberPagination


class MatchDetailView(APIView):
    """Вывод записи"""
    def get(self, request, pk):
        match = Match.objects.get(id=pk)
        serializer = MatchDetailSerializer(match)
        return Response(serializer.data)
