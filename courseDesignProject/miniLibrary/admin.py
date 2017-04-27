from django.contrib import admin
from .models import Category, Topic, TopicProfile, Comment

# Register your models here.


@admin.register(TopicProfile)
class TopicProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    fields = ('name', 'color')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    def change_select_to_published(self, request, queryset):
        opera_num = queryset.update(status='published')
        self.message_user(request, '{}篇主题已更新为\'审核通过\'!'.format(opera_num))
    def change_select_to_ban(self, request, queryset):
        opera_num = queryset.update(status='ban')
        self.message_user(request, '{}篇主题已更新为\'审核未通过\'!'.format(opera_num))

    change_select_to_published.short_description = '通过审核所选主题'
    change_select_to_ban.short_description = '审核不通过所选主题'
    actions = [change_select_to_published, change_select_to_ban]
    list_display = ('title', 'auth', 'status', 'created')
    list_fields = ('title', 'auth', 'description', 'files', 'status')
    list_filter = ('status',)
    list_editable = ('status',)



