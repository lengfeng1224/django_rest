from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from books.models import BookInfo
from books3.serializers import BookInfoSerializer


class BookListView(GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def list(self,request):
        """返回所有图书"""
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)

        return Response(serializer.data)

    def create(self,request):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response(serializer.data)
        # return Response(serializer.data,status=HTTP_404_NOT_FOUND)
        return response


