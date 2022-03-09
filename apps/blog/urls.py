from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name='post_list'),
    path("post/<slug:post_slug>", PostDetail.as_view(), name='post_detail'),
]