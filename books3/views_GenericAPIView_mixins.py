from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from books.models import BookInfo
from books3.serializers import BookInfoSerializer


class BookListView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self,request):
        # 显示所有book
        return self.list(request)


    def post(self,request):
        # 添加一个book
        # print(request.data)
        return self.create(request)

class BookView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request,pk):
        # 根据id查询其中一个book\
        # print(self.get_queryset().filter(pk=pk))
        return self.retrieve(request)

    def put(self, request,pk):
        # 根据id 区部更新一个book数据
        # print(request.data)
        return self.partial_update(request)   # 运行局部更新  可以传部分参数
        # return self.update(request)   # 必须传递所有参数

    def delete(self, request,pk):
        return self.destroy(request)