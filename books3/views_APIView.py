from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from books.models import BookInfo,HeroInfo
from .serializers import BookInfoSerializer,HeroInfoSerializer


class BookListView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books,many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)

        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response(serializer.data)
        print(response.data)
        print(response.status_code)
        print(response.status_text)
        print(response.content)
        # return Response(serializer.data,status=HTTP_404_NOT_FOUND)
        return response
