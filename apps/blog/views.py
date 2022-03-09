from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from .models import Post, Comment
# Create your views here.

class PostList(View):
    template_name = 'post_list.html'
    def get(self, request):
        context = {
            'posts': Post.objects.all()
        }
        return render(
            request,
            self.template_name,
            context
        )


class PostDetail(View):
    template_name = 'post_detail.html'
    def get(self, request, post_slug):
        post = Post.objects.get(slug=self.kwargs['post_slug'])
        context = {
            'post': post,
            'comments': post.comment.filter(parent_comment__isnull=True).all(),
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, post_slug):
        content = request.POST.get('content', None)
        parent_comment = request.POST.get('parent_comment', -1)
        if content is None:
            return Http404()

        post = Post.objects.get(slug=post_slug)
        try:
            comment = Comment.objects.get(id=parent_comment)
        except:
            comment = None
 
        Comment.objects.create(
            post=post,
            content=content,
            user=request.user,
            parent_comment=comment
        )
        context = {
            'post': post,
            'comments': post.comment.filter(parent_comment__isnull=True).all()
        }
        return render(
            request,
            self.template_name,
            context
        )