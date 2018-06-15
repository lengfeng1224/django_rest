from rest_framework import serializers
from books.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        # fields = ['id','btitle']
        fields = '__all__'

class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'
        depth = 1

class HeroInfoSerializer1(serializers.ModelSerializer):
    hbook = BookInfoSerializer
    class Meta:
        model = HeroInfo
        fields = ('id','hname','hgender','hcomment','hbook','is_delete')
        # fields = ('id','hname','hgender','hcomment','hbook')
        # 指明只能查的字段，，即只能序列化
        read_only_fields = ('hname',)
        # 添加其他的fields(todo:暂未成功) 或者改变现有的
        extra_kwargs = {
            'is_delete':{'label':'逻辑删除111', 'required':False},
            'hcomment':{'required':False}
        }



