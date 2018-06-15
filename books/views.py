from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json

from books.models import BookInfo

"""使用rest理念设计api"""
# Create your views here.
from datetime import datetime

class BooksAPIView(View):
    """
    查询所有图书,增加图书
    """
    def get(self,request):
        """
        查询所有图书
        :param request:
        :return:
        """
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                "id":book.id,
                "btitle":book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment': book.bcomment,

            })
            return JsonResponse({'data':book_list,'error':'OK'}, safe=False)

    def post(self,request):
        """
        新增图书  /books/
        :param self:
        :param request:
        :return:
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略
        book = BookInfo.objects.create(
            btitle = book_dict.get('btitle'),
            # bpub_date=datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
            bpub_date=book_dict.get('bpub_date')
        )

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,

        },status=201)

class BookAPIView(View):
    def get(self,request,id):
        """
        获取单个图书信息
        :param request:
        :param id:
        :return:
        """
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,

        })

    def put(self,request,id):
        """修改图书"""
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # todo:添加参数校验

        book.btitle = book_dict.get('btitle')
        book.bpub_date = datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,

            }
        )

    def delete(self,request,id):
        """删除图书"""
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)

