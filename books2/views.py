from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from books.models import BookInfo


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
