#coding:utf-8
from django.db import models

# Create your models here.
class Publisher(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        #指定显示在admin中显示的名称
        verbose_name = '出版社'
        verbose_name_plural = verbose_name
    name = models.CharField('名字', max_length=30)
    address = models.CharField('地址', max_length=50)
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField('省份', max_length=30)
    country = models.CharField('国家',max_length=50)
    website = models.URLField()



class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="名字")
    # 也可以在这里显式的指出在后台显示的名称
    def __str__(self):
        return self.name



class AuthorDetail(models.Model):
    def __str__(self):
        return self.author.name
    sex = models.BooleanField(max_length=1, choices=((0,'M'),(1,'F')))
    email = models.EmailField()
    #也可以把要显示的字段当成第一个参数传进去
    address = models.CharField("地址",max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)



class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2,default = 10)
