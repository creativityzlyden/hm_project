from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins
from .models import Human
from .serializers import HumanSerializer, HumanDetailSerializer
from rest_framework.pagination import PageNumberPagination


class HumanListView(generics.ListAPIView):
    """Вывод списка"""
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class HumanDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
