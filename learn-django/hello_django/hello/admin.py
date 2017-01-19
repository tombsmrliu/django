from django.contrib import admin
from hello.models import *

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'state_province', 'city')
    search_fields = ('name',)



admin.site.register(Author)
admin.site.register(AuthorDetail)


# 通过装饰器的形式注册Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
# admin.site.register(Book)

#用注册的方式注册PublisherAdmin
admin.site.register(Publisher, PublisherAdmin)
