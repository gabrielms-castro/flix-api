from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCountView(APIView):
    def get(self, request, *args, **kwargs):
        count = Review.objects.count()
        return Response({"Quantidade de Reviews:": count})  