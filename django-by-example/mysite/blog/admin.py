from django.contrib import admin
from .models import Post, Comment
# Register your models here.

# 全局响应函数，对任何的Model实例都有此选项
def show_hello(self, request, queryset):
    self.message_user(request, 'Hello,World!');
show_hello.short_description = '说你好'





# class PostAdmin start
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 编写响应函数
    def change_selected_posts_to_publish(self, request, queryset):
        operation_nums = queryset.update(status='p')
        self.message_user(request, '{}篇帖子已更新为发布状态'.format(opera))
    def change_selected_posts_to_draft(self, request, queryset):
        operation_nums = queryset.update(status='p')
        self.message_user(request, '{}篇帖子已更新为未发布状态'.format(operation_nums))
    # 设置响应函数对外的描述
    change_selected_posts_to_publish.short_description = '更改状态为已发布'
    change_selected_posts_to_draft.short_description = '更改状态为未发布'



    # 注册响应函数
    actions = [change_selected_posts_to_publish, change_selected_posts_to_draft,]
    date_hierarchy = 'created'
    # fields = ('title', 'author', 'slug')
    list_display = ('id', 'title', 'author', 'created', 'updated', 'status')
    list_filter = ('title', 'author', 'created', 'updated', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author', )
    ordering = ['status', 'publish',]
# class PostAdmin end





# class CommentAdmin start
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    raw_id_fields = ('post',)

# class CommentAdmin end


# 注册全局响应函数
admin.site.add_action(show_hello, 'say hello')
