from django.db import models
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.text import slugify
from django.http import HttpResponse, response

# Create your models here.

TOPIC_STATUS_CHOICES = (('published','审核通过'), ('wait','等待审核'), ('ban','审核不通过'))

class TopicPublishManager(models.Manager):
    def get_queryset(self):
        return super(TopicPublishManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('minilibrary:topic_list_by_category', args=[self.id])



class Topic(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    category = models.ForeignKey(Category, verbose_name='分类', related_name='topics')
    slug = models.SlugField(max_length=200, blank=True)
    files = models.FileField(verbose_name='附件', upload_to='files/%Y/%m/%d/', blank=True)
    description = models.TextField(verbose_name='详情描述', blank=True)
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', related_name='topics')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name='状态', choices=TOPIC_STATUS_CHOICES, default='wait', max_length=20)

    # 为啥这里必须加上objects，不然admin就默认使用published了
    objects = models.Manager()
    published = TopicPublishManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = '主题'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('minilibrary:topic_detail', args=[self.id])


    def get_files(self):
        return reverse('minilibrary:download_file')




class Comment(models.Model):
    topic = models.ForeignKey(Topic, related_name='comments')
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', verbose_name='作者')
    body = models.TextField(blank=True, max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL,  blank=True, related_name='comment_liked')
    total_likes = models.PositiveIntegerField(default=0)
    # status = models.CharField(verbose_name='状态', choices=TOPIC_STATUS_CHOICES)

    class Meta:
        ordering=['created',]
        verbose_name = '评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '对\'{}\'的评论.'.format(self.topic)





class TopicProfile(models.Model):
    topic = models.OneToOneField(Topic, related_name='profile')
    views = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='topic_liked')
    total_likes = models.PositiveIntegerField(default=0)
    user_bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='bookmarked')
    total_bookmarks = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = '\'主题\'面板'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '\'{}\'的信息面板'.format(self.topic)

