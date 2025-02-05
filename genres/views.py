# import json

from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Genre
from .serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


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
        
        
# # Sem Class Based View ficaria assim:
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == "GET":
#         genres = Genre.objects.all()
#         data = [{'id':genre.id, 'name':genre.name}for genre in genres]
#         return JsonResponse(data, safe=False)
    
#     elif request.method == "POST":
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {
#                 'id': new_genre.id,
#                 'name': new_genre.name
#             },
#             status=201
#         )
    

# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
    
#     if request.method == "GET":
#         data = {"id": genre.id, "name": genre.name}
#         return JsonResponse(data)
    
#     elif request.method == "PUT":
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {
#                 "id": genre.id,
#                 "name": genre.name
#             }
#         )
    
#     elif request.method == "DELETE":
#         genre.delete()
#         return JsonResponse(
#             {"message": "Gênero excluído com sucesso!"},
#             status=204
#         )