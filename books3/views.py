from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer,HeroInfoSerializer

class BookListView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books,many=True)
        return Response(serializer.data)
