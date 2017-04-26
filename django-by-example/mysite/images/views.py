from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from actions.utils import create_action


# Create your views here.



@login_required
def image_create(request):
    if request.method == 'POST':

        form = ImageCreateForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            create_action(request.user, '上传了新图片', new_item)
            messages.success(request, '图片上传成功!')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'form':form})



@login_required
def image_detail(request,id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/image_detail.html',{'image':image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST['id']
    action = request.POST['action']
    if image_id:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                create_action(request.user, '点赞了图片', image)
                image.users_like.add(request.user)
            else:
                create_action(request.user, '取消赞了图片', image)
                image.users_like.remove(request.user)
            messages.error(request, '状态更新成功!')
        except Exception as e:
            print(e)
            messages.error(request, '状态更新失败!')
    return HttpResponseRedirect(reverse('images:detail', args=[image.id, image.slug]))

@login_required
def images_list(request):
    # images = Image.objects.all()
    images = Image.objects.order_by('-total_likes')
    return render(request, 'images/image/image_list.html', {'images':images, 'section':'images'})
