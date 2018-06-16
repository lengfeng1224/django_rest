from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from books.models import BookInfo
from books3.serializers import BookInfoSerializer


class BookListView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self,request):
        books = self.get_queryset()
        serializer = self.get_serializer(books,many=True)

        return Response(serializer.data)

    def post(self,request):
        print(request.data)

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response(serializer.data)

        # return Response(serializer.data,status=HTTP_404_NOT_FOUND)
        return response
