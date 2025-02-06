from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
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
    

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse(
            {"message": "Ator excluído com sucesso!"},
            status=204
        )    

class ActorCountView(APIView):
    def get(self, request, *args, **kwargs):
        count = Actor.objects.count()
        return Response({"Quantidade de Atores:": count})
    