from django.urls import path,include
from blog.views import CategoryAPIView,PostAPIView,PostListCreateAPIView,PostRetrievUpdateDestroyAPIView

urlpatterns = [
    path('categories',CategoryAPIView.as_view()),
    path('posts',PostListCreateAPIView.as_view()),
    path('posts/<int:pk>',PostRetrievUpdateDestroyAPIView.as_view()),
    # path('posts',PostAPIView.as_view()),

]



