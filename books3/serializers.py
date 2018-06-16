from rest_framework import serializers
from books.models import BookInfo,HeroInfo

# 在序列化外也可以补充验证行为
def about_heroname(value):
    if 'xiaoming' not in value.lower():
        raise serializers.ValidationError("这个英雄的名字不是小明")


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)


    # 查看图书中所有英雄
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增

    # 补充验证
    def validate_btitle(self, value):
        """单个字段"""
        if 'django' not in value.lower():
            raise serializers.ValidationError('图书不是关于django的')
        return value
    def validate(self, attrs):
        """多个字段验证"""
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread<bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    # 保存到数据库
    def create(self, validated_data):
        """新建"""
        # 调用模型类
        book = BookInfo(**validated_data)
        book.save()  # 保持到数据库
        return book

    def update(self, instance, validated_data):
        """更新,instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle',instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date',instance.bpub_date)
        instance.bread = validated_data.get('bread',instance.bread)
        instance.bcomment = validated_data.get('bcomment',instance.bcomment)
        # 保持到数据库
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列器"""
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )
    id = serializers.IntegerField(label='ID',read_only=True)
    # 给hname 添加一个验证器
    hname = serializers.CharField(label='名字',max_length=20,validators=[about_heroname])
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES,label='性别',required=False)
    hcomment = serializers.CharField(label='描述信息',max_length=200,required=False,allow_null=True)

    # hbook = serializers.PrimaryKeyRelatedField(label='图书',read_only=True)  # 返回id
    # hbook = serializers.StringRelatedField(label='图书',read_only=True)   # 从模型类中__str__的返回
    # hbook = serializers.SlugRelatedField(label='图书', read_only=True, slug_field='bpub_date') # 指定返回字段信息
    hbook = BookInfoSerializer()
