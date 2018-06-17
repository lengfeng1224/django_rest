from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from books.models import BookInfo
from books3.serializers import BookInfoSerializer


class BookListView(CreateAPIView,ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


# class BookView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer

class BookView(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
