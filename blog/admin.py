from django.contrib import admin
from .models import Post, Author, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'published_recently')
    list_filter = ('published_date', 'author')
    inlines = [CommentInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_date')