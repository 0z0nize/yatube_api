from django.contrib import admin

from .models import Comment, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'post',
        'author',
        'text'
    )


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'pub_date',
        'author',
        'text',
        'group',
        'image'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
