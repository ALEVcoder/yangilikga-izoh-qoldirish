from django.contrib import admin
from .models import Post, Comment
# Register your models here.

# Yangilik uchun admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


# Izoh uchun admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass