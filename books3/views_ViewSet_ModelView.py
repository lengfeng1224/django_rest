
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from books.models import BookInfo
from books3.serializers import BookInfoSerializer


class BookListView(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


class BookView(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # # 自定义访问
    # def latest(self,request):
    #     """返回最新的图书信息"""
    #     book = self.get_queryset().latest('id')
    #     serializer = self.get_serializer(book)
    #     return Response(serializer.data)

