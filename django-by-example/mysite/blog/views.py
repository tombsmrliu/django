from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, PostCommentForm
from taggit.models import Tag
from django.db.models import Count




def index(request):
    return render(request, 'index.html')



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # print('the reversed url of post_list_by_tag is:' + reversed('post_list_by_tag'))
    return render(request, 'blog/post/list.html', {'page':page, 'posts':posts, 'tag':tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            slug=post,
                            status='p',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = PostCommentForm()

    post_tag_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request, 'blog/post/detail.html', {'post':post, 'comments':comments, 'comment_form':comment_form, 'similar_posts':similar_posts})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='p')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent})
