from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
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

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer    
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse(
            {"message": "Gênero excluído com sucesso!"},
            status=204
        )
        
class GenreCountView(APIView):
    def get(self, request, *args, **kwargs):
        count = Genre.objects.count()
        return Response({"Quantidade de Gêneros:": count})  
