from django.urls import path,include
from blog.views import CategoryAPIView,PostAPIView

urlpatterns = [
    path('categories',CategoryAPIView.as_view()),
    path('posts',PostAPIView.as_view()),
]
