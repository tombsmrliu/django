from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Category, Comment, TopicProfile
from django.views.decorators.http import require_POST
from .forms import TopicCreateForm, CommentForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return redirect('minilibrary:topic_list')

@login_required
def topic_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = TopicCreateForm(request.POST, request.FILES)
        files = request.FILES.get('files')
        # print(files)
        if form.is_valid():
            # form.files.save()
            topic = form.save(commit=False)
            topic.auth = request.user
            print(topic.files)
            topic.save()
            messages.success(request, '主题\'{}\'发布成功,等待管理员审核!'.format(topic.title))
            return redirect('minilibrary:topic_list')
    else:
        form = TopicCreateForm()
    return render(request, 'minilibrary/topic/topic_create.html', {'form':form, 'categories': categories})


def topic_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    topics = Topic.published.all()
    if category_id:
        try:
            # category = Category.objects.filter(id=category_id)
            category = Category.objects.get(id=category_id)
            # 注意这里的返回，之前应为使用了filter,导致返回去的是一个set,从而造成了一系列的问题
            topics = topics.filter(category=category)
        except Category.DoesNotExist: messages.error(request, '分类不存在!')
    return render(request,
                'minilibrary/topic/topic_list.html',
                {
                    'topics':topics.all,
                    'categories': categories,
                    'selectedCategory': category
                })



def topic_detail(request, topic_id):
    topic = None
    # topics = Topic.published.get(id=topic_id)
    try:
        topic = Topic.published.get(id=topic_id)
    except Topic.DoesNotExist:
        messages.error(request, "请求的帖子不存在!")
        return redirect('minilibrary:topic_list')
        # return reverse('minilibrary:topic_list')
        # 之前一直返回的事这个，所以导致了错误,reverse得到的只是一个字符串,要做的是返回一个response
        # return Response(reverse('minilibrary:topic_list')), 可以这样做，如果用reverse

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = form.save(commit=False)
                comment.auth = request.user
                comment.topic = topic
                comment.save()
                messages.success(request, '对{}的评论成功!'.format(topic))
                form = CommentForm()
            except:
                messages.error(request, '评论失败!')
    else:
        form = CommentForm()
    return render(request, 'minilibrary/topic/topic_detail.html', {'topic': topic, 'form':form})





@login_required
def download_file(request):
    return render(request, 'minilibrary/topic/download_success.html')


@login_required
def topic_like(request, topic_id):
    if request.method == 'POST':
        try:
            topic = Topic.published.get(id=topic_id)
            if request.user in topic.profile.user_likes.all():
                topic.profile.user_likes.remove(request.user)
                topic.profile.total_likes -= 1
                topic.profile.save()
                messages.success(request, '对\'{}\'取消喜爱成功!'.format(topic))
            else:
                topic.profile.user_likes.add(request.user)
                topic.profile.total_likes += 1
                topic.profile.save()
                messages.success(request, '喜爱\'{}\'成功!'.format(topic))
            return redirect(reverse('minilibrary:topic_detail', args=[topic.id]))

        except Topic.DoesNotExist:
            messages.error(request, '请求主题不存在!')
    return redirect('minilibrary:topic_list')



@login_required
def topic_bookmark(request, topic_id):
    if request.method == 'POST':
        try:
            topic = Topic.published.get(id=topic_id)
            if request.user in topic.profile.user_bookmarks.all():
                print('unbookmark')
                topic.profile.user_bookmarks.remove(request.user)
                topic.profile.total_bookmarks -= 1
                topic.profile.save()
                messages.success(request, '主题\'{}\'已从收藏夹移除!'.format(topic))
            else:
                print('bookmark')
                topic.profile.user_bookmarks.add(request.user)
                topic.profile.total_bookmarks += 1
                topic.profile.save()
                messages.success(request, '主题\'{}\'已添加进收藏夹!'.format(topic))
            return redirect(reverse('minilibrary:topic_detail', args=[topic.id]))
        except Topic.DoesNotExist:
            messages.error(request, '请求主题不存在!')
    return redirect('minilibrary:topic_list')


@login_required
def bookmark_list(request):
    user = request.user
    topicProfiles = user.bookmarked
    return render(request, 'minilibrary/topic/bookmark_manage.html', {'topicProfiles': topicProfiles})
    
    
@login_required
def remove_bookmark(request, topic_id):
    user = request.user
    try:
        topic = Topic.published.get(id=topic_id)
        if user in topic.profile.user_bookmarks.all():
            topic.profile.user_bookmarks.remove(user)
            print('删除成功')
            topic.profile.total_bookmarks -= 1
            topic.profile.save()
            messages.success(request, '\'{}\'已成功从收藏夹移除!'.format(topic))
    except:
        messages.error(request, '错误,删除失败!')
    return redirect('minilibrary:bookmark_manage')




@login_required
def topic_manage(request):
    user = request.user
    topics = user.topics
    return render(request, 'minilibrary/topic/topic_manage.html', {'topics': topics})
    
    
@login_required
def topic_remove(request, topic_id):
    user = request.user
    try:
        print(topic_id)
        topic = Topic.objects.get(id=topic_id)
        if topic in user.topics.all():
            topic_name = topic.title
            topic.delete()
            messages.success(request, '\'{}\'已成功删除!'.format(topic_name))
    except Topic.DoesNotExist:
        messages.error(request, '失败,请求帖子不存在!')
    return redirect('minilibrary:topic_manage')
    

def topic_search(request):
    word = request.GET['search_word']
    topics = Topic.published.all()
    if word:
        topics = Topic.published.filter(title__contains=word)
    return render(request, 'minilibrary/topic/topic_list.html', {'topics': topics})
        
