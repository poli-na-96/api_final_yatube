from django.contrib import admin

from .models import Comment, Group, Follow, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'created')
    search_fields = ('author', 'text')
    list_filter = ('author', 'post')
    list_display_links = ('author', 'post')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('following',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
