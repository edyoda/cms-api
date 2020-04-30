from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import CategorySerializer,PostSerializer 
from blog.models import Category,Post
# Create your views here.

class CategoryAPIView(APIView):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        ser_cat = CategorySerializer(categories,many = True)
        return Response({"categories":ser_cat.data})


class PostAPIView(APIView):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all().select_related('category')
        ser_post = PostSerializer(posts,many = True)
        return Response(ser_post.data)