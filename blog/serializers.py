
from rest_framework import serializers

from blog.models import Category
from blog.models import Post
from rest_framework.validators import UniqueValidator


# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     description = serializers.CharField()

#     def create(self,validated_data):
#         return Category.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.save()
#         return instance


# class PostSerializer(serializers.Serializer):

#     statuses = [
#         ("D","Draft"),
#         ("P","Published"),
#     ]

#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     status = serializers.ChoiceField(choices = statuses)
#     category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())

#     def create(self,validated_data):
#         return Post.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


# class PostSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     # category_name = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Post
#         fields = ['id','title','content','category','status']

#     def create(self,validated_data):
#         return Post.objects.create(**validated_data)

    # def get_category_name(self,obj):
    #     return obj.category.name


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 255, validators = [UniqueValidator(queryset=Post.objects.all())])
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id','title','content','category','status','category_name','image']

    def validate_title(self,title):
        if len(title) > 5:
            raise serializers.ValidationError("Tittle should be less than 5")
        return title 


    def get_category_name(self,obj):
        return obj.category.name