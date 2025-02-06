from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='name',
                description='Filtrar filmes pelo nome',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCountView(APIView):
    def get(self, request, *args, **kwargs):
        count = Movie.objects.count()
        return Response({"Quantidade de Filmes:": count})