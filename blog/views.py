from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import CategorySerializer,PostSerializer 
from blog.models import Category,Post
from rest_framework import status
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

    def post(self,request,*args,**kwargs):

        # get cat obj 
        # update that object for caegory key in request.data
        #
        cat_data = request.data.get("category")
        try:         
            cat_obj = Category.objects.get(id = cat_data.get('id'))
        except:
            return Response({"error":"Invalid category"},status = status.HTTP_400_BAD_REQUEST )

        ser_post = PostSerializer(data = request.data)
        
        
        # print(request.data)
        if ser_post.is_valid():
        #     # print(ser_post.is_valid())
            ser_post.validated_data['category'] = cat_obj

            post_obj = ser_post.save()
            ser_obj = PostSerializer(post_obj)
            return Response(ser_obj.data,status = status.HTTP_201_CREATED)
        else:
            return Response(ser_post.errors,status = status.HTTP_400_BAD_REQUEST)


# Post.objects.create(title = "",content = "",category = )


# Ser(obj) => data 

# Ser(data) => .save() => craete a object 
