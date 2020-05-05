from django.urls import path,include
from blog.views import CategoryAPIView,PostAPIView,PostListCreateAPIView,PostRetrievUpdateDestroyAPIView,PostViewSet,CategoryViewSet
from rest_framework import routers


blog_router = routers.DefaultRouter()
blog_router.register("posts",PostViewSet)
blog_router.register("categories",CategoryViewSet)

urlpatterns = [
    path('categories',CategoryAPIView.as_view()),
    path('',include(blog_router.urls)),
    # path('posts',PostListCreateAPIView.as_view()),
    # path('posts/<int:pk>',PostRetrievUpdateDestroyAPIView.as_view()),
    # path('posts',PostAPIView.as_view()),

]



